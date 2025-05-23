# Scoring

Scoring is decided as follows:

* There is a fixed set of possible statuses. These have a particular order (in `scoring.py`).
  Statuses include fail ❌; success ✅; notice ⚠️; and info ℹ️. 
* Each subtest can result in any of these statuses, and a numeric score/points (in the subtest execution code).
  The status is the icon displayed to the user, the points are used to weigh different subtests in total score calculation.
  Many subtests return only their full or no points, but partial points are possible and used in some subtests.
  The points are dimensionless, only used when comparing to the best possible points of the subtest
  and weighing against other subtests.
* Each subtest must declare its worst possible status (in `categories.py`).
* Each subtest must declare its best possible score/points (in `categories.py`).
* Subtests are grouped into categories.
* Each complete test run results in a total score of 0-100% shown to the user.
  (in `models.py`, particularly in `totalscore()` and
  in `checks/probes.py`, particularly `ProbeSet.count_probe_reports_score()`)
* If a subtest has FAIL as its worst status, it is included/qualified in the total score.
  Otherwise, it is entirely ignored in the calculation of scores. (`_check_mandatory_subtests()` in `categories.py`).
* If a category has any subtests that are included in the total score, the category is included in the total score.
  If a category has no such subtests, it has no impact on the total score, as if it did not exist.
* The score for a single category is determined by adding up all points in *qualifying* subtests, divided by the
  sum of the full scores declared for all these *qualifying* subtests. So the category score is a percentage of the
  max score, in that category, with possible weight differences per subtest.
* Aggregated categories (like TLS, which can have multiple tests per IP) will use the lowest/worst score of all the relevant IPs.
* In the total score, each qualifying category's score counts for an equal part. E.g. if there are two categories, with
  category X scoring 30/40 points, and Y 100/100 points, the score is (30/40 * 50%) + (100/100 * 50%) = 87.5%.
  (the 50% deriving from there being two categories). Notably, the score is _not_ 130/140 i.e. 92%.
* Note in particular that the weight in points of a particular subtests influences its weight compared to
  other subtests in the same category - not to subtests in other categories.

For clarity, a subtest is e.g. "web TLS HTTPS exists", "web appsec securitytxt", "web tls cert pubkey"
or "mail rpki valid" - it inherits from `SubTest` in `categories.py`.
A category is e.g. "web TLS" - it inherits from `Category` in `categories.py`, and contains a list of subtests.
