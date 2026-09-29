search_fore_title_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "null"
        },
        "previous": {
            "type": "null"
        },
        "results": {
            "type": "array",
            "items": [
                {
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
                            "type": "string"
                        },
                        "owner": {
                            "type": "integer"
                        },
                        "members": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "reviews": {
                            "type": "array",
                            "items": {}
                        },
                        "created": {
                            "type": "string"
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
                        "created",
                        "modified"
                    ]
                }
            ]
        }
    },
    "required": [
        "count",
        "next",
        "previous",
        "results"
    ]
}

search_fore_author_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "null"
        },
        "previous": {
            "type": "null"
        },
        "results": {
            "type": "array",
            "items": {}
        }
    },
    "required": [
        "count",
        "next",
        "previous",
        "results"
    ]
}
