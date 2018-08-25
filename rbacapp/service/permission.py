# Author: harry.cai
# DATE: 2018/7/31


def initial_session(request, permissions):
    '''
    初始化session 把用户拥有的权限放到session
    :param request:
    :param permissions:
    :return:
    '''

    permission_dict = {}
    for item in permissions:
        gid = item.get('permissions__group_id')
        if gid not in permission_dict:
            permission_dict[gid] = {
                'urls': [item['permissions__url'], ],
                "actions": [item['permissions__action'], ]
            }
        else:
            permission_dict[gid]['urls'].append(item['permissions__url'])
            permission_dict[gid]['actions'].append(item['permissions__action'])

    print(permission_dict)
    request.session['permission'] = permission_dict