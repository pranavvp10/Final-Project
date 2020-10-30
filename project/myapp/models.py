from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    addr = models.CharField(max_length=1500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class user_query(models.Model):
    user_id = models.IntegerField()
    age = models.CharField(max_length=150)
    height_cm = models.CharField(max_length=150)
    weight_kg = models.CharField(max_length=150)
    overall = models.CharField(max_length=150)
    player_positions = models.CharField(max_length=150)
    weak_foot = models.CharField(max_length=150)
    skill_moves = models.CharField(max_length=150)
    attacking_crossing = models.CharField(max_length=150)
    attacking_finishing = models.CharField(max_length=150)
    attacking_heading_accuracy = models.CharField(max_length=150)
    attacking_short_passing = models.CharField(max_length=150)
    attacking_volleys = models.CharField(max_length=150)
    skill_dribbling = models.CharField(max_length=150)
    skill_curve = models.CharField(max_length=150)
    skill_fk_accuracy = models.CharField(max_length=150)
    skill_long_passing = models.CharField(max_length=150)
    skill_ball_control = models.CharField(max_length=150)
    movement_acceleration = models.CharField(max_length=150)
    movement_sprint_speed = models.CharField(max_length=150)
    movement_agility = models.CharField(max_length=150)
    movement_reactions = models.CharField(max_length=150)
    movement_balance = models.CharField(max_length=150)
    power_shot_power = models.CharField(max_length=150)
    power_jumping = models.CharField(max_length=150)
    power_stamina = models.CharField(max_length=150)
    power_strength = models.CharField(max_length=150)
    power_long_shots = models.CharField(max_length=150)
    mentality_aggression = models.CharField(max_length=150)
    mentality_interceptions = models.CharField(max_length=150)
    mentality_positioning = models.CharField(max_length=150)
    mentality_vision = models.CharField(max_length=150)
    mentality_penalties = models.CharField(max_length=150)
    mentality_composure = models.CharField(max_length=150)
    defending_marking = models.CharField(max_length=150)
    defending_standing_tackle = models.CharField(max_length=150)
    defending_sliding_tackle = models.CharField(max_length=150)
    goalkeeping_diving = models.CharField(max_length=150)
    goalkeeping_handling = models.CharField(max_length=150)
    goalkeeping_kicking = models.CharField(max_length=150)
    goalkeeping_positioning = models.CharField(max_length=150)
    goalkeeping_reflexes = models.CharField(max_length=150)
    estimate = models.CharField(max_length=150)
    dt = models.CharField(max_length=150)
    tm = models.CharField(max_length=150)
