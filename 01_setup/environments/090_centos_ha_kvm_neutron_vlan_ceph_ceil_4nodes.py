class environment:
      data = {
        "release": 1,
        "mode": "ha_compact"
      }
      interfaces = {
        'eth0': ["public"],
        'eth1': ["private"],
        'eth2': ["storage", "management"],
        'eth3': ["fuelweb_admin"]
      }
      special_roles = {}
      node_roles = [
        ['controller', 'ceph-osd'],
        ['controller', 'ceph-osd'],
        ['controller', 'ceph-osd'],
        ['compute', 'ceph-osd']
      ]
      net_tag = {
         'management': 730,
         'storage': 732,
         'fixed': None
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
      net_cidr = {}
      net_ip_ranges = {}
      gateway = None
      bond_slaves = None
      nameservers = None
