class environment:
      data = {
        "release": 3,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "floating"],
        'eth2': ["storage", "management", "fixed"]
      }
      special_roles = {
        '52:54:00:16:74:09': ['compute']
      }
      node_roles = [
        ['controller'],
        ['cinder']
      ]
      net_tag = {
         'management': 101,
         'storage': 102,
         'fixed': 103
      }
      deploy_timeout = 120 * 60
      settings = {
        "volumes_lvm": True,
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 1
      ostf_timeout = 20 * 60
      ostf_test_sets = ['smoke', 'sanity', 'platform_tests']
      net_cidr = {
          'public': "10.16.0.1/24",
          'floating': "10.16.0.1/24"
      }
      net_ip_ranges = {}
      gateway = None
