from threading import Thread


class ThreadWorker(Thread):
    """
    This ThreadWorker is designed to be used with a queue.
    1. You populate a queue of parameters.
    2. You create a function that wants be multi-threaded, and accept the queue string as the parameter.
    3. You call the function through class_name, function_name.
    """
    def __init__(self, **kwargs):
        Thread.__init__(self)
        self.queue = kwargs.get("queue")
        self.class_name = kwargs.get("class_name")
        self.function_name = kwargs.get("function_name")
        self.kwargs = kwargs

    def run(self):
        while True:
            try:
                # This calls a function within a class, and passes args to it.
                # Example usage:
                # You have a class named Haxor: Class Haxor:
                # Within that class you have a function named hax(): def hax(something):
                # gettattr(Haxor, hax)(param)
                # getattr(Haxor, hax)("print this message")
                getattr(self.class_name, self.function_name)(param_input=self.queue.get(), **self.kwargs)
            finally:
                self.queue.task_done()
