create_success_club_schema ={
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "bookTitle": {
      "type": "string"
    },
    "bookAuthors": {
      "type": "string"
    },
    "publicationYear": {
      "type": "integer"
    },
    "description": {
      "type": "string"
    },
    "telegramChatLink": {
      "type": "string",
      "format": "uri"
    },
    "owner": {
      "type": "integer"
    },
    "members": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "reviews": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "created": {
      "type": "string",
      "format": "date-time"
    },
    "modified": {
      "type": "null"
    }
  },
  "required": [
    "id",
    "bookTitle",
    "bookAuthors",
    "publicationYear",
    "description",
    "telegramChatLink",
    "owner",
    "members",
    "reviews",
    "created"
  ]
}
create_empty_telegram_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "telegramChatLink": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "telegramChatLink"
  ]
}

create_empty_description_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "description": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "description"
  ]
}

create_empty_year_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "publicationYear": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "publicationYear"
  ]
}

create_empty_author_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "bookAuthors": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookAuthors"
  ]
}

create_empty_title_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "bookTitle": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookTitle"
  ]
}

create_club_without_authorization = {
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

create_club_without_invalid_access_token_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "detail": {
      "type": "string"
    },
    "code": {
      "type": "string"
    },
    "messages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "tokenClass": {
            "type": "string"
          },
          "tokenType": {
            "type": "string"
          },
          "message": {
            "type": "string"
          }
        },
        "required": [
          "tokenClass",
          "tokenType",
          "message"
        ]
      }
    }
  },
  "required": [
    "detail",
    "code",
    "messages"
  ]
}

update_club_schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generated Schema",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "bookTitle": {
      "type": "string"
    },
    "bookAuthors": {
      "type": "string"
    },
    "publicationYear": {
      "type": "integer"
    },
    "description": {
      "type": "string"
    },
    "telegramChatLink": {
      "type": "string",
      "format": "uri"
    },
    "owner": {
      "type": "integer"
    },
    "members": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "reviews": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "created": {
      "type": "string",
      "format": "date-time"
    },
    "modified": {
      "type": "string",
      "format": "date-time"
    }
  },
  "required": [
    "id",
    "bookTitle",
    "bookAuthors",
    "publicationYear",
    "description",
    "telegramChatLink",
    "owner",
    "members",
    "reviews",
    "created",
    "modified"
  ]
}