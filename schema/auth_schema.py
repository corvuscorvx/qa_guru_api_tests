success_auth_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "refresh": {
      "type": "string"
    },
    "access": {
      "type": "string"
    }
  },
  "required": [
    "refresh",
    "access"
  ]
}

base_error_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "detail": {
      "type": "string"
    }
  },
  "required": [
    "detail"
  ]
}

empty_fields_schema = {
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

incorrect_data_schema = base_error_schema
unsupported_media_type = base_error_schema