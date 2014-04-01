class environment:
      data = {
        "release": 1,
        "mode": "ha_compact"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "management", "storage"],
        'eth2': ["private"]
      }
      special_roles = {}
      node_roles = [
        ['controller', 'ceph-osd'],
        ['controller', 'ceph-osd'],
        ['controller', 'ceph-osd'],
        ['compute', 'ceph-osd'],
      ]
      net_tag = {
         'management': 102,
         'storage': 103,
         'public': 378,
         'floating': 378,
      }
      deploy_timeout = 180 * 60
      settings = {
        "volumes_lvm": False,
        "ceilometer": True,
        "volumes_ceph": True,
        "images_ceph": True,
        "net_provider": 'neutron',
        "net_segment_type": 'vlan',
        "neutron_vlan_range": [ 1000, 1009 ],
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 1
      ostf_timeout =  30 * 60
      ostf_test_sets = ['ha', 'smoke', 'sanity', 'platform_tests']
      net_cidr = {
          'public': "172.18.166.192/26",
          'floating': "172.18.166.192/26"
      }
      net_ip_ranges = {
          'public': [
              [
                  "172.18.166.198",
                  "172.18.166.220",
              ]
          ],
           'floating': [
              [

                  "172.18.166.221",
                  "172.18.166.250",
              ]
           ],
      }
      net_ip_ranges = {}
      gateway = None
