from rubrik_polaris import PolarisClient


domain = 'my-company'
username = 'john.doe@example.com'
password = 's3cr3tP_a55w0R)'


client = PolarisClient(domain, username, password, insecure=True)

snappables = client.get_object_ids_ec2(tags={"Environment": "staging"})
for snappable in snappables:
    snapshot = client.get_snapshots(snappable, recovery_point='latest')
    if snapshot:
        print(snapshot[0])
