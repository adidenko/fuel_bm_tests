class environment:
      data = {
        "release": 1,
        "mode": "ha_compact"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "management", "private"],
        'eth2': ["storage"]
      }
      special_roles = {
        '52:54:00:16:74:09': ['compute', 'cinder']
      }
      node_roles = [
        ['controller'],
        ['controller'],
        ['controller']
      ]
      net_tag = {
         'management': 101,
         'storage': 102,
         'fixed': 103
      }
      deploy_timeout = 180 * 60
      settings = {
        "savanna": True,
        "murano": True,
        "ceilometer": True,
        "volumes_lvm": True,
        "net_provider": 'neutron',
        "net_segment_type": 'gre',
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 11
      ostf_timeout = 6 * 60 * 60
      ostf_test_sets = ['ha', 'smoke', 'sanity', 'platform_tests']
      net_ip_ranges = {}
      gateway = None
      net_cidr = {
          'public': "10.16.0.1/24"
      }
