from hexlet_pytest.example import reverse


def test_reverse():
	assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
	assert reverse('') == ''


def test_extract_links():
    # HTML находится в файле withLinks.html в директории tests/fixtures
    with_links_path = 'tests/fixtures/Ladies_and_gentlemen.txt'
    with open(with_links_path, encoding='utf8') as f:
        html = f.read()
        # Теперь с HTML удобно работать, он не загромождает тесты
        links = reverse(html)
        assert links == '.водя и )коволешым( кешувол ищомоп ирп итсоннелсич яицялугер ,)цГк 04 акдяроп тотсач од кувзартьлу ташылс ишым ,имялетачулзи имывокувзартьлу( еинавигупто ,маткудорп к апутсод яицадивкил :ыбьроб ыреМ .))sulucsum suM( ьшым яавомод ,ремирпан( suM водор зи ишым тясонирп дерв йишьлобиаН .яинатип ыткудорп и ылаиретам тюаджервоп ,увтсйязох умонсел и умовонрез тядерВ .иицкефни еынсапо яачюлкв ,хынтовиж хиншамод и акеволеч йензелоб хигонм йелетидубзов илетинарх и вотизарап алсич огошьлоб илетисон еындорирп — ишыМ'