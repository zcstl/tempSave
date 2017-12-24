from locust import HttpLocust, TaskSet, task

class UserBh(TaskSet):
  def on_start(self):
    print 'on_start>>>'

  @task(2)
  def index(self):
    self.client.get('/')

  @task(1)
  def profile(self):
    self.client.get('/profile')

class WebUser(HttpLocust):
  task_set = UserBh
  min_wait = 5000
  max_wait = 9000
