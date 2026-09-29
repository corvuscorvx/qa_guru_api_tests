page_size_shema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "count": {
            "type": "integer"
        },
        "next": {
            "type": "string"
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
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "reviews": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                }
                            ]
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
                },
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
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "reviews": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                }
                            ]
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
                },
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
                                },
                                {
                                    "type": "integer"
                                },
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
                },
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
                },
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
                                },
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
                },
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
                },
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
                },
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
                                },
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
                },
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
                },
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
                                },
                                {
                                    "type": "integer"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "reviews": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "club": {
                                            "type": "integer"
                                        },
                                        "user": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "username": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "username"
                                            ]
                                        },
                                        "review": {
                                            "type": "string"
                                        },
                                        "assessment": {
                                            "type": "integer"
                                        },
                                        "readPages": {
                                            "type": "integer"
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
                                        "club",
                                        "user",
                                        "review",
                                        "assessment",
                                        "readPages",
                                        "created",
                                        "modified"
                                    ]
                                }
                            ]
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
