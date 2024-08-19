Khrystian Clark
        input = "passwor"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test_lowercase(self):
        input = 'PASSWORD'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'PaSSWORD'
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test_uppercase(self):
        input = 'PASSWORD'
        expected = True
        self.assertEqual(check_pwd(input), expected)
        input = 'newpassword'
        expected = False
        self.assertEqual(check_pwd(input), expected)# TDD_Hands_On
