# sample runner fix from https://github.com/scrapy/scrapyd/issues/377
from scrapy.utils.reactor import install_reactor

install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
from scrapyd.runner import main  # noqa: E402 needs after install reactor

if __name__ == "__main__":
    main()
