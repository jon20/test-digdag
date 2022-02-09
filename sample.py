import digdag

def save():
  digdag.env.store({'test_env_store': 'hoge'})

def test_task():
  raise Exception("Test Error")

