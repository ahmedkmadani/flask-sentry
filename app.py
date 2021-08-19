from logging import debug
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://e1e7409e510c41cda4302d1969a1a24b@o963914.ingest.sentry.io/5912104",
    integrations=[FlaskIntegration()],
    debug=False,
    traces_sample_rate=1.0
)


app = Flask(__name__)


@app.route('/debug_sentry')
def trigger_error():
    division_by_zero = 1/0


if __name__ == '__main__' :
    app.run(debug=True)
