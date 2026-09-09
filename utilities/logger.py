import datetime
import os

class Logger:
    file_name = ('C:\\Users\\satur\\PycharmProjects\\AutomationProject\\logs\\' +
                 str(datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')) + '.log')

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='UTF-8') as logfile:
            logfile.write(data)

    @classmethod
    def add_start_step(cls, test_name: str):
        #test_name = os.environ.get('PYTHON_CURRENT_TEST')
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        #data_to_add += f"End name method: {method}\n"
        #data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def write_url(cls, url: str):
        data_to_add = f"Final URL: {url}\n"
        cls.write_log_to_file(data_to_add)
