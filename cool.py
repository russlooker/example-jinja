import jinja2

class cool:
    def test(self,item):
        return f'from our class: {item}'
    
    def test2(self,item):
        return f'other logic here!: {item}'


templateLoader = jinja2.FileSystemLoader(searchpath = "templates/")
templateEnv = jinja2.Environment(loader=templateLoader, extensions=['jinja2.ext.do'])
template = templateEnv.get_template( 'wow.html' )
template.globals['cool'] = cool()
variableDictionary = {
    'msg':'hello world!'
    ,'mycrazy_instance':cool()
}
x = template.render( variableDictionary )
print(x)