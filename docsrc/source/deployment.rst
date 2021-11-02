Deployment
==========

Deploying ``cff`` with your function
------------------------------------

You must include the ``cff`` package when you deploy your Lambda function.

Exactly how you do this will depend on how you manage your Python project dependencies.

I use ``pipenv`` and this pattern works well for me:

.. code-block:: bash

    #!/bin/env bash
    set -euo pipefail

    # Delete previous build:
    rm -f  dist.zip
    rm -rf dist

    # Copy dependencies into "dist" directory:

    # Thanks to https://zebradil.me/post/2018-05-25-pipenv-for-aws-lambda/ for
    # this epic one-liner!
    pipenv run pip install -r <(pipenv lock -r) --target dist/

    # No need to distribute "*.dist-info":
    rm -rf dist/*.dist-info

    # Copy in my Lambda function:
    cp main.py dist

    # Create zip archive:
    cd dist
    zip -r -9 ../dist.zip ./*
    cd ..

Configuring your Lambda function
--------------------------------

Your function's *handler* should be set to ``<filename>.handler``. For example, ``main.handler`` if your script is named ``main.py``.

Lambda architecture
-------------------

**cff** is supported on ARM/Graviton2 but should work on x86 too.
