aws_storage_locations = {
    'us-east-1': 'US East (N. Virginia)',
    'us-east-2': 'US East (Ohio)',
    'us-west-1': 'US West (N. California)',
    'us-west-2': 'US West (Oregon)',
    'ca-central-1': 'Canada (Central)',
    'ap-south-1': 'Asia Pacific (Mumbai)',
    'ap-northeast-2': 'Asia Pacific (Seoul)',
    'ap-southeast-1': 'Asia Pacific (Singapore)',
    'ap-southeast-2': 'Asia Pacific (Sydney)',
    'ap-northeast-1': 'Asia Pacific (Tokyo)',
    'eu-central-1': 'EU (Frankfurt)',
    'eu-west-1': 'EU (Ireland)',
    'eu-west-2': 'EU (London)',
    'sa-east-1': 'South America (São Paulo)'
}

def get_storage_locations():
    return aws_storage_locations

def get_storage_location(region):
    return aws_storage_locations[region]

def get_storage_location_by_name(name):
    for region, location in aws_storage_locations.items():
        if location == name:
            return region
    return None

def get_storage_location_by_name_regex(name):
    for region, location in aws_storage_locations.items():
        if re.search(name, location):
            return region
    return None

