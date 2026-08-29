using System.Threading.Tasks;

public class SampleService
{
    public async Task<string> get_customer_name_async()
    {
        await Task.Delay(1);
        return "Ada";
    }
}
