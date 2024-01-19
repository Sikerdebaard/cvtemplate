import datetime


def metaskills(metaskills):
    curryear = datetime.datetime.now().year
    mastery_years = 6
    experience = {}

    mastery = lambda yoe: round(yoe / mastery_years, 2) if yoe <= mastery_years else 1.

    if 'by-year' in metaskills:
        meta = metaskills['by-year']

        for year, skills in meta.items():
            yoe = curryear - year
            pmastery = mastery(yoe)

            for skill in skills:
                experience[skill] = {'yoe': yoe, 'mastery': pmastery}

    if 'manual' in metaskills:
        meta = metaskills['manual']
        for skill, yoe in meta.items():
            experience[skill] = {'yoe': yoe, 'mastery': mastery(yoe)}

    
    texfile = '\\cvsection{SKILLS}\n\n'
    for skill in sorted(experience, key=lambda k: (experience[k]['mastery'], k), reverse=True):
        exp = experience[skill]
        texfile += f'\\cvskill{{{skill}}} {{{exp["yoe"]}+ yrs}} {{{exp["mastery"]}}} \\\\[-8pt]\n\n'
        print(skill, exp)

    return texfile
