import invokust

settings = invokust.create_settings(
    locustfile='./contrib/load_test.py',
    host='http://aguentaotranco.pythonanywhere.com',
    num_users=10,
    spawn_rate=1,
    run_time='1m'
)

loadtest = invokust.LocustLoadTest(settings)
loadtest.run()
loadtest.stats()
