import click
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
required_args = {
     'test1':int
    ,'test2':int
    ,'test3':str
    ,'test4':str
    ,'test5':int
}

def prompt_user_for_remaining_args(
        config: configparser.ConfigParser, 
        required_args:dict, 
        section:str='DEFAULT'):
    current_args = {k:v for k,v in config[section].items()}
    for k,v in required_args.items():
        if k not in current_args.keys():
            user_value = click.prompt(f'Enter a value for {k}',type=v)
            config.set(section,k,user_value)

@click.command()
def do_work():
    prompt_user_for_remaining_args(config, required_args)
    test1 = config.get('DEFAULT','test1')
    test2 = config.get('DEFAULT','test2')
    test3 = config.get('DEFAULT','test3')
    test4 = config.get('DEFAULT','test4')
    test5 = config.get('DEFAULT','test5')
    print(
        f' test1: {test1}\n'
        ,f'test2: {test2}\n'
        ,f'test3: {test3}\n'
        ,f'test4: {test4}\n'
        ,f'test5: {test5}\n'
    )


if __name__ == '__main__':
    do_work()