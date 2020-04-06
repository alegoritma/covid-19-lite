Simple, fast and free Covid-19 API. 

If you want to use just send GET request. Sevice will return data with JSON format. 

We'll add history data soon. 

Include Total Cases Per Million / Active Cases / Total Recovered / New Deaths / Death Per Million / Total Cases / Total Deaths / New Cases / Serious Critical .

# Sample Response 
      {
        "China":{
        "total_cases_per_million":57,
        "active_cases":1299,
        "total_recovered":77078,
        "new_deaths":2,
        "deaths_per_millon":2,
        "total_deaths":3331,
        "total_cases":81708,
        "new_cases":39,
        "serious_critical":265
        },
        "Peru":{
        "total_tests":19410,
        "total_cases":2281,
        "serious_critical":81,
        .
        .
        .

# Usage;

# Shell
curl --request GET \
  --url https://us-central1-covid-19-l.cloudfunctions.net/totalSummary

# Go
    import (
      "fmt"
      "net/http"
      "io/ioutil"
    )

    func main() {

      url := "https://us-central1-covid-19-l.cloudfunctions.net/totalSummary"

      req, _ := http.NewRequest("GET", url, nil)

      res, _ := http.DefaultClient.Do(req)

      defer res.Body.Close()
      body, _ := ioutil.ReadAll(res.Body)

      fmt.Println(res)
      fmt.Println(string(body))

    }
# NODE
      var http = require("https");

      var options = {
        "method": "GET",
        "hostname": "https://us-central1-covid-19-l.cloudfunctions.net",
        "port": null,
        "path": "/totalSummary",
      };

      var req = http.request(options, function (res) {
        var chunks = [];

        res.on("data", function (chunk) {
          chunks.push(chunk);
        });

        res.on("end", function () {
          var body = Buffer.concat(chunks);
          console.log(body.toString());
        });
      });

      req.end();
      
# JavaScript
      var data = null;

      var xhr = new XMLHttpRequest();
      xhr.withCredentials = true;

      xhr.addEventListener("readystatechange", function () {
        if (this.readyState === this.DONE) {
          console.log(this.responseText);
        }
      });

      xhr.open("GET", "https://us-central1-covid-19-l.cloudfunctions.net/totalSummary");
      xhr.send(data);
      
# Java
    HttpResponse<String> response = Unirest.get("https://us-central1-covid-19-l.cloudfunctions.net/totalSummary")
    .asString();
    
# Swift
      import Foundation

      let request = NSMutableURLRequest(url: NSURL(string: "https://us-central1-covid-19-l.cloudfunctions.net/totalSummary")! as URL,
                                              cachePolicy: .useProtocolCachePolicy,
                                          timeoutInterval: 10.0)
      request.httpMethod = "GET"

      let session = URLSession.shared
      let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
        if (error != nil) {
          print(error)
        } else {
          let httpResponse = response as? HTTPURLResponse
          print(httpResponse)
        }
      })

      dataTask.resume()
      
# Python
    import http.client

    conn = http.client.HTTPSConnection("https://us-central1-covid-19-l.cloudfunctions.net")

    conn.request("GET", "/totalSummary")

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
# Ruby
    require 'uri'
    require 'net/http'

    url = URI("https://us-central1-covid-19-l.cloudfunctions.net/totalSummary")

    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    http.verify_mode = OpenSSL::SSL::VERIFY_NONE

    request = Net::HTTP::Get.new(url)

    response = http.request(request)
    puts response.read_body
# Csharp
    var client = new RestClient("https://us-central1-covid-19-l.cloudfunctions.net/totalSummary");
    var request = new RestRequest(Method.GET);
    IRestResponse response = client.Execute(request);



# Contributors;
    
    * Volkan Kalın  
        GitHub: https://github.com/alegoritma/
# 
    * Said Çankıran
        GitHub: https://github.com/Scankiran
        Linkedin: https://www.linkedin.com/in/said-çankıran-b4927a160/

