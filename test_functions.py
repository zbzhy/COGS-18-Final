from functions import remove_punctuation, prepare_text, end_chat
from functions import filter_country, filter_body_type, filter_trait, result_car, compare_hp, go_back, find_source

def test_remove_punctuation():
    assert callable(remove_punctuation)
    assert type(remove_punctuation('Hello!')) == str
    assert remove_punctuation('Hello!') == 'Hello'
    assert remove_punctuation('&He@llo!') == 'Hello'

    
def test_prepare_text():
    assert callable(prepare_text)
    assert type(prepare_text('Hahaha.')) == list
    assert prepare_text('Good Morning') == ['good', 'morning']
    
    
def test_end_chat():
    assert callable(end_chat)
    assert type(end_chat('Hello')) == tuple
    assert type(end_chat('quit')) == tuple
    assert type(end_chat('quit')[0]) == str
    assert type(end_chat('Hello')[1]) == bool
    assert type(end_chat('quit')[1]) == bool
    assert end_chat('Hello') == (None, True)
    assert end_chat('quit') == ('Bye', False)
    
    
def test_filter_country():
    assert callable(filter_country)
    assert type(filter_country(1, [1, 2, 3], [4, 5, 6], target=[])) == int
    assert type(filter_country(1, [7, 8, 9], [4, 5, 6], target=[])) == str
    assert filter_country(1, [1, 2, 3], [4, 5, 6], target=[]) == 5
    assert filter_country(1, [7, 8, 9], [4, 5, 6], target=[]) == 'The car you search can not be found.'
    
    
def test_filter_body_type():
    assert callable(filter_body_type)
    assert type(filter_body_type(1, [1, 2, 3], [4, 5, 6], target=[])) == int
    assert type(filter_body_type(1, [7, 8, 9], [4, 5, 6], target=[])) == str
    assert filter_body_type(1, [1, 2, 3], [4, 5, 6], target=[]) == 5
    assert filter_body_type(1, [7, 8, 9], [4, 5, 6], target=[]) == 'Please type the body type shown in the previous list.'
    
    
def test_filter_trait():
    assert callable(filter_trait)
    assert type(filter_trait(1, [1, 2, 3], target=[])) == list
    assert type(filter_trait(1, [7, 8, 9], target=[])) == str
    assert filter_trait(1, [1, 2, 3], target=[]) == [1]
    assert filter_trait(1, [7, 8, 9], target=[]) == 'Please type the trait shown in the previous list.'
    
    
def test_result_car():
    assert callable(result_car)
    assert type(result_car('result', [2, 3], {'[2, 3]' : [4, 5]})) == list
    assert type(result_car('Hello', [2, 3], {'[2, 3]' : [4, 5]})) == str
    assert result_car('result', [2, 3], {'[2, 3]' : [4, 5]}) == [4, 5]
    assert result_car('Hello', [2, 3], {'[2, 3]' : [4, 5]}) == 'Please type [result] to find your dream car!'
    
    
def test_compare_hp():
    assert callable(compare_hp)
    assert type(compare_hp('compare', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 20})) == list
    assert type(compare_hp('Hello', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 20})) == str
    assert compare_hp('compare', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 30, 5 : 40}) == [4, 5]
    assert compare_hp('compare', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 30, 5 : 100}) == [4]
    assert compare_hp('Hello', [2, 3], {'[2, 3]' : [4, 5]}, {4 : 30, 5 : 40}) == 'Please type [compare] to find cars with similar horsepower!'
    
    
def test_go_back():
    assert callable(go_back)
    assert type(go_back('back 2', 3, [1, 2, 3])) == int
    assert go_back('back 2', 3, [1, 2, 3]) == 1
    
    
def test_find_source():
    assert callable(find_source)
    assert type(find_source([1, 2, 3])) == str
    assert find_source([1, 2, 3, 4, 5]) == 'There are so many alternatives! You can lease cars to have different experiences! https://www.leasetrader.com/'
    assert find_source([1, 2, 3]) == 'There are only few alternatives. You can find second-hand cars on sale and buy one! https://www.carmax.com/' 
    
    
    

    
    
    



                 
    