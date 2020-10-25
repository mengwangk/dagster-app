from dagster import execute_pipeline, pipeline, solid


@solid
def get_name(_):
    return "dagster"


@solid
def hello(context, name: str):
    context.log.info("Hello, {name}!".format(name=name))


@pipeline
def hello_pipeline():
    hello(get_name())


if __name__ == "__main__":
    execute_pipeline(hello_pipeline)  # Hello, dagster!
