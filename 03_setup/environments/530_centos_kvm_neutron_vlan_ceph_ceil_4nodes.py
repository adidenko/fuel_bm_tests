class environment:
      data = {
        "release": 1,
        "mode": "multinode"
      }
      interfaces = {
        'eth0': ["fuelweb_admin"],
        'eth1': ["public", "management", "storage"],
        'eth2': ["private"]
      }
      special_roles = {
        '52:54:00:16:74:09': ['compute', 'ceph-osd']
      }
      node_roles = [
        ['controller', 'ceph-osd'],
        ['cinder', 'ceph-osd']
      ]
      net_tag = {
         'management': 102,
         'storage': 103
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
          'public': "10.16.0.1/24"
      }
      net_ip_ranges = {}
      gateway = None
