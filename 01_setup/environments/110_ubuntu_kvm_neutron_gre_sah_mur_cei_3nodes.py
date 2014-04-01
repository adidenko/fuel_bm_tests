class environment:
      data = {
        "release": 3,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["public"],
        'eth1': ["private"],
        'eth2': ["storage", "management"],
        'eth3': ["fuelweb_admin"]
      }
      special_roles = {}
      node_roles = [
        ['controller'],
        ['cinder'],
        ['compute']
      ]
      net_tag = {
         'management': 730,
         'storage': 732,
         'fixed': None
      }
      deploy_timeout = 120 * 60
      settings = {
        "murano": True,
        "sahara": True,
	"ceilometer": True,
        "volumes_lvm": True,
        "net_provider": 'neutron',
        "net_segment_type": 'gre',
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 11
      ostf_timeout = 6 * 60 * 60
      ostf_test_sets = ['smoke', 'sanity', 'platform_tests']
      net_cidr = {}
      net_ip_ranges = {}
      gateway = None
      bond_slaves = None
      nameservers = None
