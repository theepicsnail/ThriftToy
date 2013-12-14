namespace py stringstore

enum Status {
  SUCCESS = 1,
  ERROR = 2
}

struct GetRequest {
  1: string key,
}

struct GetResponse {
  1: string key,
  2: optional string value,
  3: optional Status status
}

struct SetRequest {
  1: string key,
  2: string value = "",
}


service StringStore {
  GetResponse getValue(1:GetRequest req),
  oneway void setValue(1:SetRequest req),
}
