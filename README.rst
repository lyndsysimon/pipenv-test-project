Test project: pipenv dependency resolution
==========================================

What works (creating the ``Pipfile`` and ``Pipfile.lock``)
----------------------------------------------------------

Installing the dependency specified in ``setup.py`` works as expected, by
running:

    .. code-block:: bash
    PIP_PROCESS_DEPENDENCY_LINKS=1 pipenv install -e .

A ``Pipfile`` and ``Pipfile.lock`` are created, which specify the dependency
properly.

What doesn't work (installing from the ``Pipfile``/``Pipfile.lock``)
--------------------------------------------------------------------

Removing and recreating the virtualenv using the ``Pipfile``/``Pipfile.lock``
fails:

    .. code-block:: bash

    pipenv --rm
    PIP_PROCESS_DEPENDENCY_LINKS=1 pipenv install

This is the ``stdout`` output:

    .. code-block::

    Installing dependencies from Pipfile.lock (eb6742)…
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-ephem-wheel-cache-QjvTKz
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-6xR2yb
    Created requirements tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-6xR2yb'
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-install-lWs6YJ
    Collecting git-noop==1.2.3 (from -r /var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pipenv-yT7GC_-requirements/pipenv-GsEddY-requirement.txt (line 1))
      1 location(s) to search for versions of git-noop:
      * https://pypi.org/simple/git-noop/
      Getting page https://pypi.org/simple/git-noop/
      Looking up "https://pypi.org/simple/git-noop/" in the cache
      No cache entry available
      Starting new HTTPS connection (1): pypi.org:443
      https://pypi.org:443 "GET /simple/git-noop/ HTTP/1.1" 404 13
      Status code 404 not in (200, 203, 300, 301)
      Could not fetch URL https://pypi.org/simple/git-noop/: 404 Client Error: Not Found for url: https://pypi.org/simple/git-noop/ - skipping
      Could not find a version that satisfies the requirement git-noop==1.2.3 (from -r /var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pipenv-yT7GC_-requirements/pipenv-GsEddY-requirement.txt (line 1)) (from versions: )
    Cleaning up...
    Removed build tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-6xR2yb'
    No matching distribution found for git-noop==1.2.3 (from -r /var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pipenv-yT7GC_-requirements/pipenv-GsEddY-requirement.txt (line 1))
    Exception information:
    Traceback (most recent call last):
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/basecommand.py", line 141, in main
        status = self.run(options, args)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/commands/install.py", line 299, in run
        resolver.resolve(requirement_set)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 102, in resolve
        self._resolve_one(requirement_set, req)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 256, in _resolve_one
        abstract_dist = self._get_abstract_dist_for(req_to_install)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 209, in _get_abstract_dist_for
        self.require_hashes
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/operations/prepare.py", line 218, in prepare_linked_requirement
        req.populate_link(finder, upgrade_allowed, require_hashes)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/req/req_install.py", line 308, in populate_link
        self.link = finder.find_requirement(self, upgrade)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/index.py", line 543, in find_requirement
        'No matching distribution found for %s' % req
    DistributionNotFound: No matching distribution found for git-noop==1.2.3 (from -r /var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pipenv-yT7GC_-requirements/pipenv-GsEddY-requirement.txt (line 1))
    
    An error occurred while installing git-noop==1.2.3! Will try again.
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-ephem-wheel-cache-7jYUbR
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-1_aqup
    Created requirements tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-1_aqup'
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-install-x_oNVC
    Obtaining file:///Users/lyndsy/src/pipenv-test-project
      Added file:///Users/lyndsy/src/pipenv-test-project to build tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-1_aqup'
      Running setup.py (path:/Users/lyndsy/src/pipenv-test-project/setup.py) egg_info for package from file:///Users/lyndsy/src/pipenv-test-project
        Running command python setup.py egg_info
        running egg_info
        writing requirements to Test_project_for_pipenv_dependency_resolution.egg-info/requires.txt
        writing Test_project_for_pipenv_dependency_resolution.egg-info/PKG-INFO
        writing top-level names to Test_project_for_pipenv_dependency_resolution.egg-info/top_level.txt
        writing dependency_links to Test_project_for_pipenv_dependency_resolution.egg-info/dependency_links.txt
        reading manifest file 'Test_project_for_pipenv_dependency_resolution.egg-info/SOURCES.txt'
        writing manifest file 'Test_project_for_pipenv_dependency_resolution.egg-info/SOURCES.txt'
      Source in /Users/lyndsy/src/pipenv-test-project has version 1.0.0, which satisfies requirement Test-project-for-pipenv-dependency-resolution==1.0.0 from file:///Users/lyndsy/src/pipenv-test-project
      Removed Test-project-for-pipenv-dependency-resolution==1.0.0 from file:///Users/lyndsy/src/pipenv-test-project from build tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-1_aqup'
    Installing collected packages: Test-project-for-pipenv-dependency-resolution
      Found existing installation: Test-project-for-pipenv-dependency-resolution 1.0.0
        Uninstalling Test-project-for-pipenv-dependency-resolution-1.0.0:
          Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-uninstall-kYKi27
          Removing file or directory /Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/Test-project-for-pipenv-dependency-resolution.egg-link
          Removing pth entries from /Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/easy-install.pth:
          Removing entry: /Users/lyndsy/src/pipenv-test-project
          Successfully uninstalled Test-project-for-pipenv-dependency-resolution-1.0.0
      Running setup.py develop for Test-project-for-pipenv-dependency-resolution
        Running command /Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/bin/python2.7 -c "import setuptools, tokenize;__file__='/Users/lyndsy/src/pipenv-test-project/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" develop --no-deps
        running develop
        running egg_info
        writing requirements to Test_project_for_pipenv_dependency_resolution.egg-info/requires.txt
        writing Test_project_for_pipenv_dependency_resolution.egg-info/PKG-INFO
        writing top-level names to Test_project_for_pipenv_dependency_resolution.egg-info/top_level.txt
        writing dependency_links to Test_project_for_pipenv_dependency_resolution.egg-info/dependency_links.txt
        reading manifest file 'Test_project_for_pipenv_dependency_resolution.egg-info/SOURCES.txt'
        writing manifest file 'Test_project_for_pipenv_dependency_resolution.egg-info/SOURCES.txt'
        running build_ext
        Creating /Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/Test-project-for-pipenv-dependency-resolution.egg-link (link to .)
        Adding Test-project-for-pipenv-dependency-resolution 1.0.0 to easy-install.pth file
    
        Installed /Users/lyndsy/src/pipenv-test-project
    Successfully installed Test-project-for-pipenv-dependency-resolution
    Cleaning up...
    Removed build tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-1_aqup'
    
    Installing initially–failed dependencies…
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-ephem-wheel-cache-3U87Ls
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-8lW0HM
    Created requirements tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-8lW0HM'
    Created temporary directory: /private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-install-ztyR08
    Collecting git-noop==1.2.3 
      1 location(s) to search for versions of git-noop:
      * https://pypi.org/simple/git-noop/
      Getting page https://pypi.org/simple/git-noop/
      Looking up "https://pypi.org/simple/git-noop/" in the cache
      No cache entry available
      Starting new HTTPS connection (1): pypi.org:443
      https://pypi.org:443 "GET /simple/git-noop/ HTTP/1.1" 404 13
      Status code 404 not in (200, 203, 300, 301)
      Could not fetch URL https://pypi.org/simple/git-noop/: 404 Client Error: Not Found for url: https://pypi.org/simple/git-noop/ - skipping
    Cleaning up...
    Removed build tracker '/private/var/folders/nq/tmvpd65n5kl6gcw920wwmkv40000gp/T/pip-req-tracker-8lW0HM'
    Exception information:
    Traceback (most recent call last):
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/basecommand.py", line 141, in main
        status = self.run(options, args)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/commands/install.py", line 299, in run
        resolver.resolve(requirement_set)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 102, in resolve
        self._resolve_one(requirement_set, req)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 256, in _resolve_one
        abstract_dist = self._get_abstract_dist_for(req_to_install)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/resolve.py", line 209, in _get_abstract_dist_for
        self.require_hashes
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/operations/prepare.py", line 218, in prepare_linked_requirement
        req.populate_link(finder, upgrade_allowed, require_hashes)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/req/req_install.py", line 308, in populate_link
        self.link = finder.find_requirement(self, upgrade)
      File "/Users/lyndsy/.local/share/virtualenvs/pipenv-test-project-v5wOtiop/lib/python2.7/site-packages/pip/_internal/index.py", line 543, in find_requirement
        'No matching distribution found for %s' % req
    DistributionNotFound: No matching distribution found for git-noop==1.2.3 
