class environment:
      data = {
        "release": 2,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["public", "storage", "management"],
        'eth1': ["fuelweb_admin", "private"]
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
        "net_segment_type": 'vlan',
        "neutron_vlan_range": [ 475, 479 ],
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
