
#URL FOR EACH ROUTE
UserPost = "https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany"
CustomerPost = "https://mf-api-customer-nccrp.ondigitalocean.app/api/customers/addMany"
CustomerGet = "https://mf-api-customer-nccrp.ondigitalocean.app/api/customers/addMany"
TagPut = ""
RolePut = ""
RulePost = ""
FlowPost = ""

#HTTP header
post_header = {"Content-Type": "application/json"}
get_header = {'Authorization': 'access_token myToken'}


#JSON FILE SCHEMA
UserSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "CreatedAt" : {"type" : "string"},
        "Password" : {"type" : "string"},
        "Username" : {"type" : "string"},
        "Email" : {"type" : "string"},
        "Role" : {"type" : "string"},
        "Status" : {"type" : "string"},
        "Leads" : {"type" : "string"},
        "Team" : {"type" : "string"},
        "DivisionName" : {"type" : "string"},
        "LastLogin" : {"type" : "string"},
        "Authority" : {"type" : "string"},
        "Channels" : {"type" : "string"},
        "ChannelInfo" : {"type" : "string"},
        "Phone" : {"type" : "string"},
    },
}

User_Auth = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "Dashboard" : {"type" : "boolean"},
        "Livechat" : {"type" : "boolean"},
        "Contact" : {"type" : "boolean"},
        "Boardcast" : {"type" : "boolean"},
        "Flowbuilder" : {"type" : "boolean"},
        "Integrations" : {"type" : "boolean"},
        "ProductCatalogue" : {"type" : "boolean"},
        "Organization" : {"type" : "boolean"},
        "Admin" : {"type" : "boolean"},
    }
}

User_Info = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "Phone" : {"type" : "string"},
        "Address" : {"type" : "string"},
        "ChannelId" : {"type" : "string"},
    }
}

CustomerSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "ID" : {"type" : "string"},
        "Name" : {"type" : "string"},
        "FirstName" : {"type" : "string"},
        "LastName" : {"type" : "string"},
        "Phones" : {"type" : "array", "items" : {"type" : "string"}},
        "Organization" : {"type" : "string"},
        "Channels" : {"type" : "array", "items" : {"type" : "string"}},
        
        "Group" : {"type" : "string"},
        "Team" : {"type" : "string"},
        "Agents" : {"type" : "array", "items" : {"type" : "string"}},
        "Tags" : {"type" : "array", "items" : {"type" : "string"}},
        "Birthday" : {"type" : "string"},
        "Country" : {"type" : "string"},
        "Address" : {"type" : "string"},
        "CreatedAt" : {"type" : "string"},
        "UpdatedAt" : {"type" : "string"},
    }
}

RoleSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "Name" : {"type" : "string"},
        "Dashboard" : {"type" : "boolean"},
        "Livechat" : {"type" : "boolean"},
        "Contact" : {"type" : "boolean"},
        "Boardcast" : {"type" : "boolean"},
        "Flowbuilder" : {"type" : "boolean"},
        "Integrations" : {"type" : "boolean"},
        "ProductCatalogue" : {"type" : "boolean"},
        "Organization" : {"type" : "boolean"},
        "Admin" : {"type" : "boolean"},
    }
}

TagSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "type" : "array",
    "properties" : {
        "ID" : {"type" : "string"},
        "Tags" : {"type" : "string"},
        "Total" : {"type" : "number"},
        "Created" : {"type" : "string"},
        "Updated" : {"type" : "string"},
    }
}

RuleSchema = {}

FlowSchema = {}
