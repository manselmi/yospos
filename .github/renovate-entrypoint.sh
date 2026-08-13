#!/usr/bin/env sh
# vim: set ft=sh :

# Stop at any error and treat unset vars as errors.
set -o errexit
set -o nounset


curl() {
  /usr/bin/curl --fail --location --max-time 10 --no-progress-meter --retry 2 "${@}"
}


MISE_INSTALL="$(mktemp)"
MISE_DIR="${HOME}/.local/bin"
MISE="${MISE_DIR}/mise"

curl --output "${MISE_INSTALL}" -- 'https://mise.jdx.dev/install.sh'
chmod -- +x "${MISE_INSTALL}"
env -- \
  MISE_INSTALL_PATH="${MISE}" \
  MISE_INSTALL_SKIP_IF_EXISTS=1 \
  MISE_QUIET=1 \
  "${MISE_INSTALL}"


exec env -- \
  MISE_GITHUB_TOKEN="${RENOVATE_TOKEN}" \
  PATH="${MISE_DIR}:${PATH}" \
  renovate
