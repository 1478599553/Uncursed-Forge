using System;
using System.Net.Http;

var baseAddress = new Uri("https://addons-ecs.forgesvc.net");

using var httpClient = new HttpClient { BaseAddress = baseAddress };
{
    {
        using (var response = await httpClient.GetAsync("/api/v2/addon/310806/description"))
        {
            string responseHeaders = response.Headers.ToString();
            string responseData = await response.Content.ReadAsStringAsync();

            Console.WriteLine("Status " + (int)response.StatusCode);
            Console.WriteLine("Headers " + responseHeaders);
            Console.WriteLine("Data " + responseData);
        }
    }
}