class environment:
      data = {
        "release": 1,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["public", "storage", "management"],
        'eth1': ["fuelweb_admin"]
      }
      special_roles = {}
      node_roles = [
        ['controller'],
        ['cinder', 'mongo'],
        ['compute']
      ]
      net_tag = {
         'management': 471,
         'storage': 472
      }
      deploy_timeout = 120 * 60
      settings = {
        "volumes_lvm": True,
        "volumes_ceph": False,
        "images_ceph": False,
        "murano": True,
        "sahara": True,
        "ceilometer": True,
        "net_provider": 'neutron',
        "net_segment_type": 'gre',
        "libvirt_type": "kvm",
        "additional_kernel_params": "ipmi_si.tryacpi=0 ipmi_si.trydmi=0 ipmi_si.trydefaults=0"
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
