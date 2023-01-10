import re


def solve_a(*args):
    m_ore = max(args[1], args[2], args[3], args[5])
    m_clay = args[4]
    m_obs = args[6]
    o = [ ( t - 1 ) * t // 2 for t in range( 32 + 1 ) ]

    max_geo = 0

    def dfs(time, goal,
            ore_r, clay_r=0, obs_r=0, geo_r=0,
            ore=0, clay=0, obs=0, geo=0):
        nonlocal max_geo
        # Prune
        if goal == 0 and ore_r >= m_ore:
            return
        elif goal == 1 and clay_r >= m_clay:
            return
        elif goal == 2 and (clay_r == 0 or obs_r >= m_obs):
            return
        elif goal == 3 and obs_r == 0:
            return
        elif geo + geo_r * time + o[time] <= max_geo:
            return
        while time:
            if goal == 0 and ore >= args[1]:
                for g in range(4):
                    dfs(time - 1, g, ore_r + 1, clay_r, obs_r, geo_r,
                        ore - args[1] + ore_r, clay + clay_r, obs + obs_r, geo + geo_r)
                return
            elif goal == 1 and ore >= args[2]:
                for g in range(4):
                    dfs(time - 1, g, ore_r, clay_r + 1, obs_r, geo_r,
                        ore - args[2] + ore_r, clay + clay_r, obs + obs_r, geo + geo_r)
                return
            elif goal == 2 and ore >= args[3] and clay >= args[4]:
                for g in range(4):
                    dfs(time - 1, g, ore_r, clay_r, obs_r + 1, geo_r,
                        ore - args[3] + ore_r, clay - args[4] + clay_r, obs + obs_r, geo + geo_r)
                return
            elif goal == 3 and ore >= args[5] and obs >= args[6]:
                for g in range(4):
                    dfs(time - 1, g, ore_r, clay_r, obs_r, geo_r + 1,
                        ore - args[5] + ore_r, clay + clay_r, obs - args[6] + obs_r, geo + geo_r)
                return
            time, ore, clay, obs, geo = time - 1, ore + ore_r, clay + clay_r, obs + obs_r, geo + geo_r

        max_geo = max(max_geo, geo)

    for goal in range(4):
        dfs(32, goal, 1)

    return max_geo


if __name__ == '__main__':
    rows = open("19.txt").read().split('\n')
    total = 1
    for i, row in enumerate(rows):
        print(i)
        vals = list(map(int, re.findall(r"(\d+)", row)))
        # print(vals)

        total *= solve_a(*vals)

    print(total)
