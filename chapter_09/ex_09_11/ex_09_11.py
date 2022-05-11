import user

admin_privileges = ["can add post", "can remove post", "can ban users"]
admin_1 = user.Admin("martia", "harmartia", "fatalflaw39", 80)
admin_1.privileges.set_privilege_list(admin_privileges)
admin_1.describe_user()
admin_1.privileges.add_privilege("can alter posts")
admin_1.privileges.show_privileges()
