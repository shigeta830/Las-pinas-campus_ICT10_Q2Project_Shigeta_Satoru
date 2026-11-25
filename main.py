from pyscript import document, when

# ==========================================
# 1. SEATWORK 1: CREW / CANDIDATE CHECK
# ==========================================
CLUB_MEMBERS = [
    "bong bong marcos",
    "ethan de leon",
    "spider man",
    "jose rizal",
    "ibbara",
]


def update_sw1_console(text, mode="neutral"):
    box = document.getElementById("sw1_result")
    if not box:
        return
    box.className = "lc-console"
    if mode == "success":
        box.classList.add("success")
    elif mode == "denied":
        box.classList.add("denied")
    box.innerHTML = text


@when("click", "#sw1_check_btn")
def check_sw1_candidate(event):
    f_el = document.getElementById("first_name")
    l_el = document.getElementById("last_name")
    if not f_el or not l_el:
        return
    candidate = f"{f_el.value.strip()} {l_el.value.strip()}".strip()
    if not candidate:
        update_sw1_console("WARNING: ENTER FIRST AND LAST NAME.", "denied")
        return
    if candidate.lower() in CLUB_MEMBERS:
        update_sw1_console(
            f"MISSION PASSED // WELCOME, {candidate.upper()}!",
            "success",
        )
    else:
        update_sw1_console(
            f"ACCESS DENIED // {candidate.upper()} IS NOT ON THE LIST.",
            "denied",
        )


@when("click", "#sw1_reset_btn")
def reset_sw1(event):
    f_el = document.getElementById("first_name")
    l_el = document.getElementById("last_name")
    if f_el and l_el:
        f_el.value = ""
        l_el.value = ""
    update_sw1_console("AWAITING PLAYER INPUT...", "neutral")


@when("click", ".sw1-slot")
def fill_sw1_slot(event):
    btn = event.currentTarget
    f_el = document.getElementById("first_name")
    l_el = document.getElementById("last_name")
    if f_el and l_el:
        f_el.value = btn.getAttribute("data-first") or ""
        l_el.value = btn.getAttribute("data-last") or ""
    check_sw1_candidate(event)


# ==========================================
# 2. SKILLS TEST: ELEMENT CHECKER
# ==========================================
NON_METAL = {
    "H": ("Hydrogen", "1", "1.008"),
    "He": ("Helium", "2", "4.003"),
    "C": ("Carbon", "6", "12.011"),
    "N": ("Nitrogen", "7", "14.007"),
    "O": ("Oxygen", "8", "15.999"),
    "F": ("Fluorine", "9", "18.998"),
    "Ne": ("Neon", "10", "20.180"),
    "P": ("Phosphorus", "15", "30.974"),
    "S": ("Sulfur", "16", "32.06"),
    "Cl": ("Chlorine", "17", "35.45"),
    "Ar": ("Argon", "18", "39.948"),
    "Se": ("Selenium", "34", "78.971"),
    "Br": ("Bromine", "35", "79.904"),
    "Kr": ("Krypton", "36", "83.798"),
    "I": ("Iodine", "53", "126.90"),
    "Xe": ("Xenon", "54", "131.29"),
    "Rn": ("Radon", "86", "222"),
}


@when("click", "#search_btn")
def show_element(event):
    inp = document.getElementById("element_input")
    out = document.getElementById("Result")
    if not inp or not out:
        return
    symbol = inp.value.strip().capitalize()
    name, atomic_num, atomic_mass = NON_METAL.get(
        symbol,
        ("Element not found", "-", "-"),
    )
    out.innerHTML = f"""
    <b>Symbol:</b> {symbol}<br>
    <b>Element:</b> {name}<br>
    <b>Atomic Number:</b> {atomic_num}<br>
    <b>Atomic Mass:</b> {atomic_mass}
    """


# ==========================================
# 3. MEET THE CREATOR DOSSIER (Edit yours!)
# ==========================================
CREATOR = {
    "name": "Satoru Shigeta",
    "section": "Grade 10 • ICT",
    "interests": [
        "PC games & system optimization",
        "Cooking & trying new recipes",
        "Learning languages & building projects",
    ],
    "hobbies": [
        "Gaming",
        "Working out & walking",
        "Cooking",
    ],
    "dream": "Finish strong this quarter, keep improving my skills, and build things I'm proud of.",
    "quote": "Every big city starts one block at a time.",
}


def render_creator_dossier():
    box = document.getElementById("creator_dossier")
    if not box:
        return
    interests_html = "".join(f"<li>{i}</li>" for i in CREATOR["interests"])
    hobbies_html = "".join(f"<li>{h}</li>" for h in CREATOR["hobbies"])
    box.innerHTML = f"""
      <div class="d-flex flex-wrap justify-content-between align-items-center mb-3 pb-3 border-bottom border-secondary">
        <div>
          <span class="lc-kicker">Player Profile</span>
          <h2 class="lc-title h3 mb-0">{CREATOR["name"]}</h2>
        </div>
        <span class="badge text-bg-warning fs-6">{CREATOR["section"]}</span>
      </div>
      <div class="row g-4 mb-4">
        <div class="col-md-6">
          <h3 class="h6 lc-card-header">Interests</h3>
          <ul class="mb-0">{interests_html}</ul>
        </div>
        <div class="col-md-6">
          <h3 class="h6 lc-card-header">Hobbies</h3>
          <ul class="mb-0">{hobbies_html}</ul>
        </div>
      </div>
      <div class="mb-4">
        <h3 class="h6 lc-card-header">Dreams &amp; Goals</h3>
        <p class="mb-0">{CREATOR["dream"]}</p>
      </div>
      <div class="lc-console">
        <span class="text-warning">FAVORITE QUOTE:</span> “{CREATOR["quote"]}”
      </div>
    """


render_creator_dossier()
