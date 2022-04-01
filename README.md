# hdoc-tracker [20/47]

## TODO

- [x] GitHub actions
- [x] Streak count (longest and current)
- [x] extract more entities (link to src, demo, etc.)
- [x] list view
  - [x] timestamp
  - [x] extra entities (demo, src, etc.)
  - [x] Link to original tweet
- [x] thread view
  - [x] YouTube reply clone
- [ ] Keyboard shortcuts dialog + ? binding to display it
- [x] improve color contrast (thanks to VisBug)
- [ ] pytest
  - [x] at least have some tests
  - [ ] 80% coverage
  - [x] coverage
  - [ ] GitHub Actions
- [ ] jest unit tests
  - [x] at least have some tests
  - [ ] 80% coverage
  - [ ] GitHub Actions
- [ ] cypress
- [x] routing
- [ ] refactor UI code
- [ ] refactor backend code
- [x] responsive
- [x] mobile friendly
- [x] Search functionality
- [x] dark mode
- [-] adaptive SVG favicon
- [ ] SVG className instead of other state prop
- [ ] performance measurement
  - [ ] get_tweets time taken (incremental fetch already?)
  - [ ] Lighthouse Mobile score
  - [ ] Lighthouse Desktop score
- [ ] performance improvements
- [ ] about page with Mermaid https://www.youtube.com/watch?v=6TiIrJf63Xs
- [ ] support for new rounds (backend)
  - [ ] folder-based?
  - [ ] Filter by round
  - [ ] need an API for new rounds (or for the sake of learning 😏)
- [ ] support for new rounds (UI)
- [ ] more entity support
  - [ ] npm
  - [ ] pypi
  - [ ] rust package
  - [ ] go package

## bugs

- [x] time zone bug in `formatTwitterDate` function
- [x] no streaks, but display the most recent streak instead

## useful resources

- mocking Date in jest
  - https://github.com/facebook/jest/issues/2234#issuecomment-731451275
- crop PNG
  - https://www.iloveimg.com/crop-image/crop-png

## layout resource, inspirations

- grid layout with side navigation rails
  - https://developer.chrome.com/
