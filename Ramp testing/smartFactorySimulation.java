package smartFactory;

import java.time.Duration;
import java.util.*;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;
import io.gatling.javaapi.jdbc.*;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;
import static io.gatling.javaapi.jdbc.JdbcDsl.*;

public class smartFactorySimulation extends Simulation {

  private HttpProtocolBuilder httpProtocol = http
    .baseUrl("https://events.gw.postman.com")
    .inferHtmlResources(AllowList(), DenyList(".*\\.js", ".*\\.css", ".*\\.gif", ".*\\.jpeg", ".*\\.jpg", ".*\\.ico", ".*\\.woff", ".*\\.woff2", ".*\\.(t|o)tf", ".*\\.png", ".*\\.svg", ".*detectportal\\.firefox\\.com.*"))
    .acceptHeader("*/*")
    .acceptEncodingHeader("gzip, deflate, br")
    .acceptLanguageHeader("en-US,en;q=0.9")
    .contentTypeHeader("application/x-www-form-urlencoded; charset=UTF-8")
    .originHeader("https://web.postman.co")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36");
  

  

  

  


  
  private String uri2 = "https://events.launchdarkly.com/events/bulk/60645109ece3b60c64ac5e02";
  
  private String uri3 = "https://events.getpostman.com/events";
  
  private String uri4 = "https://web.postman.co/_api/ws/proxy";
  
  private String uri5 = "https://bam.nr-data.net/ins/1/NRJS-8482e4e3e1750395f5d";

  private ScenarioBuilder scn = scenario("smartFactorySimulation")
    .exec(
      http("request_0")
        .post("/")
        .formParam("checksum", "70ac6f3feb79e6756bf20ff98af86b69")
        .formParam("client", "56d4a7f42486e1c4ec95a892fd96c402")
        .formParam("e", "[{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687075824,\"event_id\":50,\"session_id\":1700686259657,\"event_type\":\"Workspace Sidebar - Collections - Clicked\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{\"cta_type\":\"other\",\"user_id\":27504721,\"app_version\":\"10.20.3-231120-0418\",\"release_channel\":\"prod\",\"platform\":\"browser\",\"current_url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"event_source\":\"client_app\",\"team_user_id\":\"27504721\",\"user_domain_professional\":false,\"user_email_verified\":true,\"company_size\":0,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"workspace_visibility\":\"personal\",\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\"},\"user_properties\":{},\"uuid\":\"d47a962e-3917-44e2-932d-8f18f7fa4c9d\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":121,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}},{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687075831,\"event_id\":72,\"session_id\":1700686259657,\"event_type\":\"$identify\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{},\"user_properties\":{\"$set\":{\"userId\":27504721,\"exp_growth_133_collection_copy_link_button\":\"off\",\"user_id\":27504721,\"app_version\":\"10.20.3-231120-0418\",\"release_channel\":\"prod\",\"platform\":\"browser\",\"current_url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"event_source\":\"client_app\",\"team_user_id\":\"27504721\",\"user_domain_professional\":false,\"user_email_verified\":true,\"company_size\":0,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"workspace_visibility\":\"personal\",\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\"}},\"uuid\":\"91174adc-67bd-48cd-8258-30ce73e6746b\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":122,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}},{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687075843,\"event_id\":73,\"session_id\":1700686259657,\"event_type\":\"$identify\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{},\"user_properties\":{\"$set\":{\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\"}},\"uuid\":\"b9a8c080-05a6-4c2d-bfcd-3c2cb58fa3fb\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":123,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}},{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687075843,\"event_id\":51,\"session_id\":1700686259657,\"event_type\":\"Request Page - Viewed\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{\"referrer\":\"\",\"is_forked\":false,\"url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"user_id\":27504721,\"app_version\":\"10.20.3-231120-0418\",\"release_channel\":\"prod\",\"platform\":\"browser\",\"current_url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"event_source\":\"client_app\",\"team_user_id\":\"27504721\",\"user_domain_professional\":false,\"user_email_verified\":true,\"company_size\":0,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"workspace_visibility\":\"personal\",\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\"},\"user_properties\":{},\"uuid\":\"6b40da89-19e8-49b7-985b-34373ce05650\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":124,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}}]")
        .formParam("upload_time", "1700687076616")
        .formParam("v", "2")
    )
    .pause(1)
    .exec(
      http("request_1")
        .post(uri4)
        .body(RawFileBody("smartFactory/smartfactorysimulation/0001_request.json"))
        .resources(
          http("request_2")
            .post(uri2)
            .body(RawFileBody("smartFactory/smartfactorysimulation/0002_request.json")),
          http("request_3")
            .post("/")
            .formParam("checksum", "be5560604c7e08de829050bdc043019b")
            .formParam("client", "56d4a7f42486e1c4ec95a892fd96c402")
            .formParam("e", "[{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687078260,\"event_id\":74,\"session_id\":1700686259657,\"event_type\":\"$identify\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{},\"user_properties\":{\"$set\":{\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\"}},\"uuid\":\"f9e050e6-1147-4aaa-87b3-cec52e7f58ae\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":125,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}}]")
            .formParam("upload_time", "1700687078260")
            .formParam("v", "2"),
          http("request_4")
            .post("/")
            .formParam("checksum", "fa5f616fcd61c357a37b9004d6c9abbe")
            .formParam("client", "56d4a7f42486e1c4ec95a892fd96c402")
            .formParam("e", "[{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687078262,\"event_id\":52,\"session_id\":1700686259657,\"event_type\":\"Send Request - Clicked\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{\"cta_text\":\"Send\",\"cta_style\":\"custom\",\"cta_type\":\"button\",\"is_test_present\":false,\"user_id\":27504721,\"app_version\":\"10.20.3-231120-0418\",\"release_channel\":\"prod\",\"platform\":\"browser\",\"current_url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"event_source\":\"client_app\",\"team_user_id\":\"27504721\",\"user_domain_professional\":false,\"user_email_verified\":true,\"company_size\":0,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"workspace_visibility\":\"personal\",\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\"},\"user_properties\":{},\"uuid\":\"4b18ac8c-f682-44ac-983e-d848fa2cc417\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":126,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}}]")
            .formParam("upload_time", "1700687078382")
            .formParam("v", "2")
        )
    )
    .pause(1)
    .exec(
      http("request_5")
        .post("/")
        .formParam("checksum", "5ef8c6eb33ece04c95abf615f44adcc6")
        .formParam("client", "56d4a7f42486e1c4ec95a892fd96c402")
        .formParam("e", "[{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687080265,\"event_id\":75,\"session_id\":1700686259657,\"event_type\":\"$identify\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{},\"user_properties\":{\"$set\":{\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\"}},\"uuid\":\"b4bda4ed-a650-4bfa-be73-c1763af58b63\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":127,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}}]")
        .formParam("upload_time", "1700687080266")
        .formParam("v", "2")
        .resources(
          http("request_6")
            .post("/")
            .formParam("checksum", "868a89af2c01525373bea7aad9283f82")
            .formParam("client", "56d4a7f42486e1c4ec95a892fd96c402")
            .formParam("e", "[{\"device_id\":\"VXRdfDnomwQ9Gohfq95I8n\",\"user_id\":\"27504721\",\"timestamp\":1700687080267,\"event_id\":53,\"session_id\":1700686259657,\"event_type\":\"Send Request - Clicked\",\"version_name\":null,\"platform\":\"Web\",\"os_name\":\"Chrome\",\"os_version\":\"119\",\"device_model\":\"Mac OS\",\"device_manufacturer\":null,\"language\":\"en-US\",\"api_properties\":{},\"event_properties\":{\"cta_text\":\"Send\",\"cta_style\":\"custom\",\"cta_type\":\"button\",\"is_test_present\":false,\"user_id\":27504721,\"app_version\":\"10.20.3-231120-0418\",\"release_channel\":\"prod\",\"platform\":\"browser\",\"current_url\":\"workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f\",\"event_source\":\"client_app\",\"team_user_id\":\"27504721\",\"user_domain_professional\":false,\"user_email_verified\":true,\"company_size\":0,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"workspace_visibility\":\"personal\",\"exp_growth_grw_837_organize_notifications\":\"variation\",\"exp_growth_grw_658_a_a_test\":\"off\",\"exp_growth_289_enable_team_discovery\":\"unassigned\",\"exp_growth_133_collection_copy_link_button\":\"off\"},\"user_properties\":{},\"uuid\":\"3e537db5-1e76-421b-9131-33b01c67b362\",\"library\":{\"name\":\"amplitude-js\",\"version\":\"8.15.0\"},\"sequence_number\":128,\"groups\":{},\"group_properties\":{},\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36\",\"plan\":{\"branch\":\"main\",\"source\":\"web\",\"version\":\"264.0.0\"}}]")
            .formParam("upload_time", "1700687080399")
            .formParam("v", "2")
        )
    )
    .pause(3)
    .exec(
      http("request_7")
        .post(uri3)
        .body(RawFileBody("smartFactory/smartfactorysimulation/0007_request.json"))
    )
    .pause(2)
    .exec(
      http("request_8")
        .post(uri4)
        .body(RawFileBody("smartFactory/smartfactorysimulation/0008_request.json"))
    )
    .pause(7)
    .exec(
      http("request_9")
        .post(uri5 + "?a=771436762&sa=1&v=1216.487a282&t=Unnamed%20Transaction&rst=580907&ck=0&ref=https://web.postman.co/workspace/My-Workspace~665f3756-9f1a-46df-8fb9-e76af3b97375/request/27504721-79be619f-16d9-45e6-807e-ce612a54075f")
        .body(RawFileBody("smartFactory/smartfactorysimulation/0009_request.bin"))
    );

  {
	  setUp(scn.injectOpen(rampUsers(10).during(20))).protocols(httpProtocol);
  }
}
