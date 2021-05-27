impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {        
        let mut str1 = String::from("");
        let mut str2 = String::from("");
        for part in word1.iter() {
            str1.push_str(part)
        }
        for part in word2.iter() {
            str2.push_str(part)
        }
        return str1 == str2;
    }
}
