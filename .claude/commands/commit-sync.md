---
description: Inspect the repo, create the correct logical commit(s), and safely sync with the remote
---

Inspect the current Git repository, create the correct logical commit(s), and synchronize safely with the configured remote.

Follow this workflow strictly:

1. Inspect repository state:

```bash
git status --short
git status
git branch --show-current
git remote -v
git log --oneline --decorate -5
git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null || true
```

2. Fetch remote state:

```bash
git fetch --prune
git status -sb
git rev-list --left-right --count HEAD...@{u} 2>/dev/null || true
```

Do not assume the branch is synchronized. Verify it.

3. Inspect all changes before staging:

```bash
git diff --stat
git diff
git diff --cached --stat
git diff --cached
git status --short
```

Also inspect relevant untracked files/directories sufficiently to understand what they contain.

4. Determine:

* what changed;
* whether all changes belong to one logical commit;
* whether anything is unrelated, generated, temporary, or sensitive;
* the correct Conventional Commit type and optional scope.

Preferred commit format:

```text
<type>(<scope>): <concise imperative summary>

<optional explanation of what changed and why>
```

Use types such as:
`feat`, `fix`, `refactor`, `test`, `docs`, `ci`, `build`, `chore`, `perf`.

Do not use vague messages such as:
`update files`, `changes`, `all`, `fix stuff`.

Do not automatically add AI attribution or `Co-Authored-By` trailers.

5. Stage intentionally.

Prefer explicit paths. Only use `git add -A` when every current change has been verified to belong to the same commit.

Then verify exactly what will be committed:

```bash
git status --short
git diff --cached --stat
git diff --cached
```

6. Commit using the selected Conventional Commit message.

Then verify:

```bash
git show --stat --oneline --decorate HEAD
git status
```

7. Before pushing, check remote state again:

```bash
git fetch --prune
git status -sb
git rev-list --left-right --count HEAD...@{u} 2>/dev/null || true
```

If local and remote unexpectedly diverged, do not force, reset, rebase, amend, or overwrite history. Stop and explain the exact state.

8. Push safely:

```bash
git push
```

If no upstream exists and the intended remote is clearly `origin`:

```bash
git push -u origin "$(git branch --show-current)"
```

Never force-push.

9. Verify synchronization after push:

```bash
git fetch --prune
git status
git status -sb
git rev-list --left-right --count HEAD...@{u}
git log -1 --oneline --decorate
git rev-parse HEAD
git rev-parse @{u}
```

Only claim success when:

* the push succeeded;
* the working tree is clean;
* local/upstream count is `0 0`;
* `HEAD` and upstream resolve to the same commit.

Final response should be concise:

```text
Committed and synchronized.

Commit:
`<sha> <commit title>`

Branch:
`<branch>`

Upstream:
`<remote>/<branch>`

Verification:
- push succeeded
- working tree clean
- local/upstream: 0 0
- HEAD equals upstream
```

If there is nothing to commit, do not create an empty commit. Verify whether the branch still needs pushing and synchronize if necessary.
