class environment:
      data = {
        "release": 1,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "management", "private"],
	'eth2': ["storage"]
      }
      special_roles = {
        '52:54:00:16:74:09': ['compute', 'ceph-osd']
      }
      node_roles = [
        ['controller', 'ceph-osd'],
        ['cinder', 'ceph-osd']
      ]
      net_tag = {
         'management': 101
      }
      deploy_timeout = 120 * 60
      settings = {
        "volumes_lvm": False,
        "volumes_ceph": True,
        "images_ceph": True,
        "murano": True,
        "savanna": True,
        "ceilometer": True,
        "net_provider": 'neutron',
        "net_segment_type": 'gre',
        "libvirt_type": "kvm"
      }
      ostf_should_fail = 11
      ostf_timeout = 6 * 60 * 60
      ostf_test_sets = ['smoke', 'sanity', 'platform_tests']
      net_cidr = {
          'public': "10.16.0.1/24"
      }
      net_ip_ranges = {}
      gateway = None
