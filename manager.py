from sphere import Sphere
import utils

GRAVITY = [0.0,1000.0]

def applyGravity(sphere):
    sphere.accelerate(GRAVITY)

def update(sph_arr, dt):
    substeps = 20
    sub_dt = dt / substeps
    for i in range(substeps):
        for sphere in sph_arr:
            applyGravity(sphere)
            sphere.applyConstraints()
            resolve_collisions(sph_arr, sphere)
            sphere.updatePos(sub_dt)

def resolve_collisions(sph_arr, sphere):
    for other in sph_arr:
        distance = utils.get_distance(sphere.pos_current, other.pos_current)
        if distance < sphere.size + other.size and not sphere.equals(other):
            collision_axis = utils.get_unit_vec(sphere.pos_current, other.pos_current)
            change_distance = (sphere.size + other.size) - distance

            change_vec = utils.mult_scalar(collision_axis, change_distance/2)
            sphere.pos_current = utils.add(sphere.pos_current, change_vec)
            other.pos_current = utils.sub(other.pos_current, change_vec)
