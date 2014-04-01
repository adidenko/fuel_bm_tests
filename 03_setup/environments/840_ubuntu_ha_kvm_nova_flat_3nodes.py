class environment:
      data = {
        "release": 3,
        "mode": "ha_compact"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "floating"],
        'eth2': ["storage", "management", "fixed"]
      }
      special_roles = {}
      node_roles = [
        ['controller', 'cinder'],
        ['controller', 'cinder'],
        ['controller', 'cinder'],
        ['compute']
      ]
      net_tag = {
         'public': 378,
         'floating': 378,
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
      gateway = None
