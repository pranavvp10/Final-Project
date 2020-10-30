from django.shortcuts import render
from .models import user_login,user_details,user_query
from django.db.models import Max
from datetime import datetime
from project.settings import BASE_DIR

# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request,'./myapp/about.html')

def contact(request):
    return render(request,'./myapp/contact.html')

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd)

        if len(ul) == 1:
            request.session['user_id'] = ul[0].uname
            context = {'uname': request.session['user_id']}
            return render(request, 'myapp/admin_home.html',
                          context)
        else:
            return render(request, 'myapp/admin_login.html')
    else:
        return render(request, 'myapp/admin_login.html')

def admin_home(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_home.html',context)

def admin_settings(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings.html',context)

def admin_settings_404(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings_404.html',context)

def admin_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_id']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/admin_settings.html')
            else:
                return render(request, './myapp/admin_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/admin_changepassword.html')
    else:
        return render(request, './myapp/admin_changepassword.html')

########USER#############
def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/user_home.html',context)
        else:

            return render(request, 'myapp/user_login.html')
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)

def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, addr=addr, pin=pin, contact=contact,
                               status=status,email=email )
        ud.save()

        print(user_id)

        return render(request, 'myapp/user_login.html')

    else:
        return render(request, 'myapp/user_details_add.html')

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/user_settings.html')
            else:
                return render(request, './myapp/user_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/user_changepassword.html')
    else:
        return render(request, './myapp/user_changepassword.html')

def user_settings(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_settings.html',context)

import os
from . import player_test
def user_query_add(request):
    if request.method == 'POST':

        age = request.POST.get('age')
        height_cm = request.POST.get('height_cm')
        weight_kg = request.POST.get('weight_kg')
        #overall= request.POST.get('overall')
        player_positions = request.POST.get('player_positions')
        weak_foot = request.POST.get('weak_foot')
        skill_moves = request.POST.get('skill_moves')
        attacking_crossing = request.POST.get('attacking_crossing')
        attacking_finishing = request.POST.get('attacking_finishing')
        attacking_heading_accuracy = request.POST.get('attacking_heading_accuracy')
        attacking_short_passing = request.POST.get('attacking_short_passing')
        attacking_volleys = request.POST.get('attacking_volleys')
        skill_dribbling = request.POST.get('skill_dribbling')
        skill_curve = request.POST.get('skill_curve')
        skill_fk_accuracy = request.POST.get('skill_fk_accuracy')
        skill_long_passing = request.POST.get('skill_long_passing')
        skill_ball_control = request.POST.get('skill_ball_control')
        movement_acceleration = request.POST.get('movement_acceleration')
        movement_sprint_speed = request.POST.get('movement_sprint_speed')
        movement_agility = request.POST.get('movement_agility')
        movement_reactions = request.POST.get('movement_reactions')
        movement_balance = request.POST.get('movement_balance')
        power_shot_power = request.POST.get('power_shot_power')
        power_jumping = request.POST.get('power_jumping')
        power_stamina = request.POST.get('power_stamina')
        power_strength = request.POST.get('power_strength')
        power_long_shots = request.POST.get('power_long_shots')
        mentality_aggression = request.POST.get('mentality_aggression')
        mentality_interceptions = request.POST.get('mentality_interceptions')
        mentality_positioning = request.POST.get('mentality_positioning')
        mentality_vision = request.POST.get('mentality_vision')
        mentality_penalties = request.POST.get('mentality_penalties')
        mentality_composure = request.POST.get('mentality_composure')
        defending_marking = request.POST.get('defending_marking')
        defending_standing_tackle = request.POST.get('defending_standing_tackle')
        defending_sliding_tackle = request.POST.get('defending_sliding_tackle')
        goalkeeping_diving = request.POST.get('goalkeeping_diving')
        goalkeeping_handling = request.POST.get('goalkeeping_handling')
        goalkeeping_kicking = request.POST.get('goalkeeping_kicking')
        goalkeeping_positioning = request.POST.get('goalkeeping_positioning')
        goalkeeping_reflexes = request.POST.get('goalkeeping_reflexes')
        ###################################################################

        input_set = [float(age),float(height_cm),float(weight_kg),float(weak_foot),
                        float(skill_moves),float(attacking_crossing),float(attacking_finishing),
                        float(attacking_heading_accuracy),float(attacking_short_passing),
                        float(attacking_volleys),float(skill_dribbling),float(skill_curve),
                        float(skill_fk_accuracy),float(skill_long_passing),float(skill_ball_control),
                        float(movement_acceleration),float(movement_sprint_speed),float(movement_agility),
                        float(movement_reactions),float(movement_balance),float(power_shot_power),
                        float(power_jumping),float(power_stamina),float(power_strength),float(power_long_shots),
                        float(mentality_aggression),float(mentality_interceptions),float(mentality_positioning),
                        float(mentality_vision),float(mentality_penalties),float(mentality_composure),float(defending_marking),
                        float(defending_standing_tackle),float(defending_sliding_tackle),float(goalkeeping_diving),
                        float(goalkeeping_handling),float(goalkeeping_kicking),float(goalkeeping_positioning),
                        float(goalkeeping_reflexes)]
        data_file_path = os.path.join(BASE_DIR, 'data/data.csv')
        tr_file = data_file_path
        result = player_test.player_prediction(training_file=tr_file, input_set=input_set)
        overall = player_test.player_prediction2(training_file=tr_file, input_set=input_set)
        print(result)

        estimate  = str(result)

        ####################################################################
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        user_id = request.session['user_id']
        ud = user_query(user_id=user_id, age=age,goalkeeping_handling=goalkeeping_handling,
                        overall=overall,weight_kg=weight_kg,height_cm=height_cm,
                        skill_moves=skill_moves,weak_foot=weak_foot,player_positions=player_positions,
                        attacking_finishing=attacking_finishing,attacking_crossing=attacking_crossing,
                        attacking_heading_accuracy=attacking_heading_accuracy,
                        attacking_short_passing=attacking_short_passing,
                        skill_dribbling=skill_dribbling,attacking_volleys=attacking_volleys,
                        skill_fk_accuracy=skill_fk_accuracy,skill_curve=skill_curve,
                        skill_ball_control=skill_ball_control,skill_long_passing=skill_long_passing,
                        movement_sprint_speed=movement_sprint_speed,movement_acceleration=movement_acceleration,
                        movement_reactions=movement_reactions,movement_agility=movement_agility,
                        power_long_shots=power_long_shots,power_strength=power_strength,power_shot_power=power_shot_power,
                        power_stamina=power_stamina,power_jumping=power_jumping,movement_balance=movement_balance,
                        mentality_interceptions=mentality_interceptions,mentality_aggression=mentality_aggression,
                        mentality_vision=mentality_vision,mentality_positioning=mentality_positioning,
                        goalkeeping_diving=goalkeeping_diving,defending_sliding_tackle=defending_sliding_tackle,
                        defending_standing_tackle=defending_standing_tackle,defending_marking=defending_marking,
                        mentality_composure=mentality_composure,mentality_penalties=mentality_penalties,
                        goalkeeping_kicking=goalkeeping_kicking,goalkeeping_positioning=goalkeeping_positioning, goalkeeping_reflexes=goalkeeping_reflexes, dt=dt, tm=tm, estimate=estimate)
        ud.save()

        context = {'msg': 'Player avg transfer value estimated (euros)','estimate':estimate,'msg2': 'Player overall performance value estimated','overall':overall}
        return render(request, 'myapp/user_query_add.html',context)
    else:
        context = {}

        return render(request, 'myapp/user_query_add.html',context)

def user_query_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    lm = user_query.objects.get(id=int(id))
    lm.delete()
    return user_query_view(request)

def user_query_view(request):
    user_id = request.session['user_id']
    ush_l = user_query.objects.filter(user_id=int(user_id))

    context = {'search_list': ush_l}
    return render(request, 'myapp/user_query_view.html', context)
