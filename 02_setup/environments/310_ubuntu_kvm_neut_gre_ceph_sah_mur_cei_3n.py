class environment:
      data = {
        "release": 2,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["public", "storage", "management"],
        'eth1': ["fuelweb_admin"]
      }
      special_roles = {
        '00:26:6c:f2:dc:41': ['mongo'],
      }
      node_roles = [
        ['controller', 'ceph-osd'],
        ['compute', 'ceph-osd']
      ]
      net_tag = {
         'management': 471,
         'storage': 472
      }
      deploy_timeout = 120 * 60
      settings = {
        "volumes_lvm": False,
        "volumes_ceph": True,
        "images_ceph": True,
        "murano": True,
        "sahara": True,
        "ceilometer": True,
        "net_provider": 'neutron',
        "net_segment_type": 'gre',
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 4
      ostf_timeout = 6 * 60 * 60
      ostf_test_sets = ['smoke', 'sanity', 'platform_tests']
      
      net_cidr = {
          'public': "10.16.122.0/24",
      }
      net_ip_ranges = {
      }
      gateway = None
      nameservers = None
      bond_slaves = None
