registration_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "username": {
      "type": "string"
    },
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "remoteAddr": {
      "type": "string",
      "format": "ipv4"
    }
  },
  "required": [
    "id",
    "username",
    "firstName",
    "lastName",
    "email",
    "remoteAddr"
  ]
}

base_error_registration_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "username": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "password": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": []
}

existing_registration_schema = base_error_registration_schema
empty_registration_schema = base_error_registration_schema
