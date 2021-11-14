from datetime import time


post_header = {"Content-Type": "application/json"}
get_header = {'Authorization': 'access_token myToken'}

User = {
    "type" : "object",
    "properties" : {
        "CreatedAt" : {"type" : "string"},
        "Password" : {"type" : "string"},
        "UserName" : {"type" : "string"},
        "Email" : {"type" : "string"},
        "Role" : {"type" : "string"},
        "Status" : {"type" : "string"},
        "Leads" : {"type" : "string"},
        "Team" : {"type" : "string"},
        "DivisionName" : {"type" : "string"},
        "LastLogin" : {"type" : "string"},
        "Authority" : {"type" : "object"},
        "Channels" : {"type" : "array", "items" : {"type" : "string"}},
        "ChannelInfo" : {"type" : "ojecct"},
        "Phone" : {"type" : "string"},
    }
}

User_Auth = {
    "type" : "object",
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
    "type" : "object",
    "properties" : {
        "Phone" : {"type" : "string"},
        "Address" : {"type" : "string"},
        "ChannelId" : {"type" : "string"},
    }
}

Customer = {
    "type" : "object",
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
        "CreatedAt" : {"type" : "number"},
        "UpdatedAt" : {"type" : "number"},
    }
}

Role = {
    "type" : "object",
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