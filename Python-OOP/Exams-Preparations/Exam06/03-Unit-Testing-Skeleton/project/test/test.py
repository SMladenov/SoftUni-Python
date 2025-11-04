import unittest
from project.social_media import SocialMedia

class SocialMediaTests (unittest.TestCase):

    def setUp (self):
        self.socialMedia = SocialMedia("Kirilcho", "Instagram", 12, "Fitness")
    
    def test_constructor_all_valid (self):
        self.assertEqual(self.socialMedia._username, "Kirilcho")
        self.assertEqual(self.socialMedia._platform, "Instagram")
        self.assertEqual(self.socialMedia._followers, 12)
        self.assertEqual(self.socialMedia._content_type, "Fitness")
        self.assertEqual(self.socialMedia._posts, [])
    
    def test_platform_property_raises (self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as msg:
            SocialMedia("Kirilcho", "SomeRandomPlatform", 12, "Fitness")
        self.assertEqual(str(msg.exception), f"Platform should be one of {allowed_platforms}")
    
    def test_followers_property_raises (self):
        with self.assertRaises(ValueError) as msg:
            self.socialMedia.followers = -1
        self.assertEqual(str(msg.exception), "Followers cannot be negative.")
    
    def test_create_post_valid (self):
        result = self.socialMedia.create_post("FirstPost")
        #new_post = {'content': post_content, 'likes': 0, 'comments': []}
        self.assertEqual(result, f"New {self.socialMedia._content_type} post created by {self.socialMedia._username} on {self.socialMedia._platform}.")
        resultDict = ""
        for dict in self.socialMedia._posts:
            for key, value in dict.items():
                if key == 'content' and value == 'FirstPost':
                    resultDict = 'FirstPost'
        self.assertEqual("FirstPost", resultDict)

    def test_like_post_out_of_range (self):
        result = self.socialMedia.like_post(-1)
        self.assertEqual(result, "Invalid post index.")
    
    def test_like_post_valid (self):
        self.socialMedia.create_post("FirstPost")
        result = self.socialMedia.like_post(0)
        self.assertEqual(result, f"Post liked by {self.socialMedia._username}.")
    
    def test_like_post_maximum_likes (self):
        self.socialMedia.create_post("FirstPost")
        for dict in self.socialMedia._posts:
            for key, value in dict.items():
                if key == 'content' and value == 'FirstPost':
                    dict['likes'] = 10
        result = self.socialMedia.like_post(0)
        self.assertEqual(result, f"Post has reached the maximum number of likes.")

    def test_comment_on_post_not_long_enough (self):
        self.socialMedia.create_post("FirstPost")
        result = self.socialMedia.comment_on_post(0, "TooShortC")
        self.assertEqual(result, "Comment should be more than 10 characters.")
    
    def test_comment_on_post_all_valid (self):
        self.socialMedia.create_post("FirstPost")
        result = self.socialMedia.comment_on_post(0, "NormalComment")
        self.assertEqual(result, f"Comment added by {self.socialMedia._username} on the post.")

if __name__ == '__main__':
    unittest.main()