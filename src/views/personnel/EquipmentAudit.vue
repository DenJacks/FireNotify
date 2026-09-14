<template>
  <div class="w-full min-w-0 space-y-6">

    <!-- ========================================================= -->
    <!-- HEADER -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">
      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-5">

        <div>
          <p class="text-sm font-semibold text-[#8B1E23]">
            FIRENOTIFY PERSONNEL PORTAL
          </p>

          <h2 class="text-2xl font-bold text-slate-900 mt-1">
            Equipment Audit
          </h2>

          <p class="text-sm text-slate-500 mt-1 max-w-2xl">
            Monitor equipment availability, condition, assignment,
            inspection, and maintenance records.
          </p>
        </div>

        <button
          @click="openAddModal"
          class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D] transition flex items-center justify-center gap-2"
        >
          <span class="text-lg leading-none">+</span>
          Add Equipment
        </button>

      </div>
    </section>


    <!-- ========================================================= -->
    <!-- STATISTICS -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">

      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Total Equipment
        </p>

        <p class="text-3xl font-bold text-slate-900 mt-2">
          {{ totalEquipment }}
        </p>

        <p class="text-xs text-slate-400 mt-2">
          Station inventory
        </p>
      </div>


      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Serviceable
        </p>

        <p class="text-3xl font-bold text-green-600 mt-2">
          {{ serviceableCount }}
        </p>

        <p class="text-xs text-green-600 font-semibold mt-2">
          {{ serviceablePercentage }}% operational
        </p>
      </div>


      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          For Maintenance
        </p>

        <p class="text-3xl font-bold text-yellow-600 mt-2">
          {{ maintenanceCount }}
        </p>

        <p class="text-xs text-slate-400 mt-2">
          Needs inspection or repair
        </p>
      </div>


      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-sm">
        <p class="text-sm text-slate-500">
          Critical Issues
        </p>

        <p class="text-3xl font-bold text-[#8B1E23] mt-2">
          {{ criticalCount }}
        </p>

        <p
          class="text-xs font-semibold mt-2"
          :class="criticalCount > 0 ? 'text-red-600' : 'text-green-600'"
        >
          {{ criticalCount > 0 ? 'Immediate attention' : 'No critical issues' }}
        </p>
      </div>

    </section>


    <!-- ========================================================= -->
    <!-- FILTERS -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-5">

      <div class="flex flex-col lg:flex-row lg:items-end gap-4">

        <!-- CATEGORY -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Equipment Category
          </label>

          <select
            v-model="categoryFilter"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option>All Categories</option>
            <option
              v-for="category in availableCategories"
              :key="category"
              :value="category"
            >
              {{ category }}
            </option>
          </select>
        </div>


        <!-- CONDITION -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Condition
          </label>

          <select
            v-model="conditionFilter"
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 bg-white text-sm text-slate-700 outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
          >
            <option>All Conditions</option>
            <option>Serviceable</option>
            <option>For Maintenance</option>
            <option>Damaged</option>
            <option>Missing</option>
            <option>Audit Required</option>
          </select>
        </div>


        <!-- SEARCH -->
        <div class="flex-1">
          <label class="text-sm font-semibold text-slate-700">
            Search Inventory
          </label>

          <div class="relative mt-2">

            <svg
              class="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-slate-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"
              />
            </svg>

            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search equipment..."
              class="w-full pl-9 pr-4 py-3 rounded-xl border border-slate-300 bg-white text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20 focus:border-[#8B1E23]"
            />

          </div>
        </div>


        <!-- CLEAR -->
        <button
          @click="clearFilters"
          class="px-5 py-3 rounded-xl border border-slate-300 text-sm font-bold text-slate-600 hover:bg-slate-50 transition"
        >
          Clear
        </button>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- INVENTORY + SIDE PANEL -->
    <!-- ========================================================= -->
    <section class="grid grid-cols-1 xl:grid-cols-3 gap-6">

      <!-- INVENTORY -->
      <div class="xl:col-span-2 bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 border-b border-slate-200 pb-4">

          <div>
            <h3 class="text-lg font-bold text-slate-900">
              Equipment Inventory
            </h3>

            <p class="text-sm text-slate-500 mt-1">
              Current station equipment records
            </p>
          </div>

          <span class="px-3 py-1.5 rounded-full bg-blue-50 text-blue-700 text-xs font-bold">
            {{ filteredEquipment.length }} Items
          </span>

        </div>


        <div class="mt-5 space-y-4">

          <div
            v-for="equipment in filteredEquipment"
            :key="equipment.id"
            class="p-5 rounded-xl border transition hover:shadow-sm"
            :class="getCardClass(equipment.condition)"
          >

            <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4">

              <div class="flex gap-4 min-w-0">

                <!-- ICON -->
                <div
                  class="h-11 w-11 rounded-xl flex items-center justify-center shrink-0"
                  :class="getIconBackground(equipment.condition)"
                >
                  <span
                    v-html="getEquipmentIcon(equipment.condition)"
                    class="h-5 w-5"
                    :class="getIconColor(equipment.condition)"
                  ></span>
                </div>


                <!-- DETAILS -->
                <div class="min-w-0">

                  <div class="flex flex-wrap items-center gap-2">

                    <p class="text-base font-bold text-slate-900">
                      {{ equipment.name }}
                    </p>

                    <span class="text-xs font-semibold text-slate-400">
                      {{ equipment.id }}
                    </span>

                  </div>

                  <p class="text-sm text-slate-500 mt-1">
                    {{ equipment.category }} · {{ equipment.location }}
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    Assigned to:
                    <span class="font-semibold text-slate-700">
                      {{ equipment.assignedTo }}
                    </span>
                  </p>

                  <p class="text-sm text-slate-500 mt-1">
                    Last inspected:
                    {{ equipment.lastInspected }}
                  </p>

                  <p
                    v-if="equipment.nextInspection"
                    class="text-sm text-slate-500 mt-1"
                  >
                    Next inspection:
                    {{ equipment.nextInspection }}
                  </p>

                  <p
                    v-if="equipment.notes"
                    class="text-sm text-slate-500 mt-1"
                  >
                    {{ equipment.notes }}
                  </p>

                </div>

              </div>


              <!-- RIGHT -->
              <div class="flex flex-col sm:items-end gap-3">

                <span
                  class="w-fit px-3 py-1.5 rounded-full text-xs font-bold"
                  :class="getStatusClass(equipment.condition)"
                >
                  {{ equipment.condition }}
                </span>

                <div class="flex flex-wrap gap-2 sm:justify-end">

                  <button
                    @click="viewEquipment(equipment)"
                    class="px-3 py-2 rounded-lg border border-slate-200 bg-white text-xs font-bold text-slate-600 hover:bg-slate-100"
                  >
                    View
                  </button>

                  <button
                    @click="editEquipment(equipment)"
                    class="px-3 py-2 rounded-lg border border-slate-200 bg-white text-xs font-bold text-slate-600 hover:bg-slate-100"
                  >
                    Edit
                  </button>

                  <button
                    v-if="equipment.condition !== 'Serviceable'"
                    @click="markInspected(equipment.id)"
                    class="px-3 py-2 rounded-lg bg-[#8B1E23] text-white text-xs font-bold hover:bg-[#72181D]"
                  >
                    Mark Inspected
                  </button>

                  <button
                    v-if="equipment.condition === 'Serviceable'"
                    @click="reportIssue(equipment)"
                    class="px-3 py-2 rounded-lg border border-red-200 text-red-600 text-xs font-bold hover:bg-red-50"
                  >
                    Report Issue
                  </button>

                </div>

              </div>

            </div>

          </div>


          <!-- EMPTY -->
          <div
            v-if="filteredEquipment.length === 0"
            class="text-center py-12"
          >
            <div
              class="mx-auto h-12 w-12 rounded-full bg-slate-100 flex items-center justify-center"
            >
              <svg
                class="h-6 w-6 text-slate-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m21 21-4.35-4.35m2.1-5.4a7.5 7.5 0 1 1-15 0 7.5 7.5 0 0 1 15 0Z"
                />
              </svg>
            </div>

            <p class="mt-3 text-sm font-semibold text-slate-700">
              No equipment found
            </p>

            <p class="text-xs text-slate-500 mt-1">
              Try changing your filters or search term.
            </p>
          </div>

        </div>

      </div>


      <!-- ======================================================= -->
      <!-- SIDE PANEL -->
      <!-- ======================================================= -->
      <div class="space-y-6">

        <!-- AUDIT PROGRESS -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <h3 class="text-lg font-bold text-slate-900">
            Audit Progress
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Monthly inventory verification
          </p>

          <div class="mt-5">

            <div class="flex items-end justify-between">

              <p class="text-3xl font-bold text-[#8B1E23]">
                {{ auditProgress }}%
              </p>

              <span class="text-xs font-semibold text-green-600">
                {{ inspectedCount }} of {{ totalEquipment }} checked
              </span>

            </div>

            <div class="mt-3 h-3 rounded-full bg-slate-200 overflow-hidden">

              <div
                class="h-full bg-[#8B1E23] rounded-full transition-all duration-500"
                :style="{ width: `${auditProgress}%` }"
              ></div>

            </div>

            <p class="text-xs text-slate-500 mt-3">
              {{ remainingAudit }} item{{ remainingAudit === 1 ? '' : 's' }}
              still require inspection or verification.
            </p>

          </div>

        </div>


        <!-- UPCOMING MAINTENANCE -->
        <div class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

          <div class="flex items-center justify-between">

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                Upcoming Maintenance
              </h3>

              <p class="text-sm text-slate-500 mt-1">
                Equipment requiring attention
              </p>
            </div>

            <span class="px-2.5 py-1 rounded-full bg-yellow-50 text-yellow-700 text-xs font-bold">
              {{ maintenanceItems.length }}
            </span>

          </div>


          <div class="mt-5 space-y-4">

            <div
              v-for="item in maintenanceItems"
              :key="item.id"
              class="p-4 rounded-xl border"
              :class="item.urgent ? 'bg-red-50 border-red-200' : 'bg-yellow-50 border-yellow-200'"
            >

              <p class="text-sm font-bold text-slate-900">
                {{ item.name }}
              </p>

              <p
                class="text-xs font-semibold mt-1"
                :class="item.urgent ? 'text-red-700' : 'text-yellow-700'"
              >
                Due {{ item.dueDate }}
              </p>

              <p class="text-xs text-slate-500 mt-1">
                {{ item.note }}
              </p>

            </div>


            <div
              v-if="maintenanceItems.length === 0"
              class="text-center py-6"
            >
              <p class="text-sm font-semibold text-green-600">
                No upcoming maintenance
              </p>

              <p class="text-xs text-slate-500 mt-1">
                All equipment is currently up to date.
              </p>
            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- COMPLIANCE -->
    <!-- ========================================================= -->
    <section class="bg-white border border-slate-200 rounded-2xl shadow-sm p-6">

      <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">

        <div>
          <h3 class="text-lg font-bold text-slate-900">
            Equipment Compliance
          </h3>

          <p class="text-sm text-slate-500 mt-1">
            Station equipment readiness and audit completion
          </p>
        </div>

        <p
          class="text-3xl font-bold"
          :class="complianceRate >= 80 ? 'text-green-600' : 'text-yellow-600'"
        >
          {{ complianceRate }}%
        </p>

      </div>


      <div class="mt-4 h-3 rounded-full bg-slate-200 overflow-hidden">

        <div
          class="h-full rounded-full transition-all duration-500"
          :class="complianceRate >= 80 ? 'bg-green-500' : 'bg-yellow-500'"
          :style="{ width: `${complianceRate}%` }"
        ></div>

      </div>


      <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 mt-5">

        <div>
          <p class="text-xs text-slate-500">
            Serviceable
          </p>

          <p class="text-xl font-bold text-green-600 mt-1">
            {{ serviceableCount }}
          </p>
        </div>

        <div>
          <p class="text-xs text-slate-500">
            Maintenance
          </p>

          <p class="text-xl font-bold text-yellow-600 mt-1">
            {{ maintenanceCount }}
          </p>
        </div>

        <div>
          <p class="text-xs text-slate-500">
            Damaged / Missing
          </p>

          <p class="text-xl font-bold text-[#8B1E23] mt-1">
            {{ criticalCount }}
          </p>
        </div>

        <div>
          <p class="text-xs text-slate-500">
            Audit Completion
          </p>

          <p class="text-xl font-bold text-blue-600 mt-1">
            {{ auditProgress }}%
          </p>
        </div>

      </div>

    </section>


    <!-- ========================================================= -->
    <!-- ADD / EDIT MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="showFormModal"
      class="fixed inset-0 z-50 bg-black/40 flex items-center justify-center p-4"
      @click.self="closeFormModal"
    >

      <div
        class="w-full max-w-2xl bg-white rounded-2xl shadow-2xl overflow-hidden"
      >

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23] uppercase tracking-wide">
              Equipment Record
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ editingEquipment ? 'Edit Equipment' : 'Add Equipment' }}
            </h3>
          </div>

          <button
            @click="closeFormModal"
            class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-500"
          >
            ✕
          </button>

        </div>


        <form
          @submit.prevent="saveEquipment"
          class="p-6 grid grid-cols-1 sm:grid-cols-2 gap-4"
        >

          <div>
            <label class="text-sm font-semibold text-slate-700">
              Equipment Name
            </label>

            <input
              v-model="form.name"
              required
              type="text"
              placeholder="Example: Fire Hose Reel"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Equipment ID
            </label>

            <input
              v-model="form.id"
              required
              type="text"
              placeholder="Example: FH-002"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Category
            </label>

            <select
              v-model="form.category"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            >
              <option>Firefighting Tools</option>
              <option>Protective Equipment</option>
              <option>Communication</option>
              <option>Medical Supplies</option>
              <option>Rescue Tools</option>
              <option>Vehicle Equipment</option>
            </select>
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Condition
            </label>

            <select
              v-model="form.condition"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            >
              <option>Serviceable</option>
              <option>For Maintenance</option>
              <option>Damaged</option>
              <option>Missing</option>
              <option>Audit Required</option>
            </select>
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Location
            </label>

            <input
              v-model="form.location"
              required
              type="text"
              placeholder="Equipment Bay"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Assigned To
            </label>

            <input
              v-model="form.assignedTo"
              required
              type="text"
              placeholder="Personnel / Vehicle / Station"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Last Inspected
            </label>

            <input
              v-model="form.lastInspected"
              type="date"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div>
            <label class="text-sm font-semibold text-slate-700">
              Next Inspection
            </label>

            <input
              v-model="form.nextInspection"
              type="date"
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none focus:ring-2 focus:ring-[#8B1E23]/20"
            />
          </div>


          <div class="sm:col-span-2">

            <label class="text-sm font-semibold text-slate-700">
              Notes
            </label>

            <textarea
              v-model="form.notes"
              rows="3"
              placeholder="Additional equipment information..."
              class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none resize-none focus:ring-2 focus:ring-[#8B1E23]/20"
            ></textarea>

          </div>


          <div class="sm:col-span-2 flex justify-end gap-3 pt-2">

            <button
              type="button"
              @click="closeFormModal"
              class="px-5 py-3 rounded-xl border border-slate-300 text-sm font-bold text-slate-600 hover:bg-slate-50"
            >
              Cancel
            </button>

            <button
              type="submit"
              class="px-5 py-3 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              {{ editingEquipment ? 'Save Changes' : 'Add Equipment' }}
            </button>

          </div>

        </form>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- VIEW DETAILS MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="selectedEquipment"
      class="fixed inset-0 z-50 bg-black/40 flex items-center justify-center p-4"
      @click.self="selectedEquipment = null"
    >

      <div class="w-full max-w-xl bg-white rounded-2xl shadow-2xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200 flex items-center justify-between">

          <div>
            <p class="text-xs font-bold text-[#8B1E23] uppercase tracking-wide">
              Equipment Details
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-1">
              {{ selectedEquipment.name }}
            </h3>
          </div>

          <button
            @click="selectedEquipment = null"
            class="h-9 w-9 rounded-lg hover:bg-slate-100 text-slate-500"
          >
            ✕
          </button>

        </div>


        <div class="p-6 space-y-5">

          <div class="flex items-center justify-between">

            <span class="text-sm font-semibold text-slate-500">
              Equipment Status
            </span>

            <span
              class="px-3 py-1.5 rounded-full text-xs font-bold"
              :class="getStatusClass(selectedEquipment.condition)"
            >
              {{ selectedEquipment.condition }}
            </span>

          </div>


          <div class="grid grid-cols-2 gap-4">

            <div class="rounded-xl bg-slate-50 p-4">
              <p class="text-xs text-slate-500">
                Equipment ID
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedEquipment.id }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-4">
              <p class="text-xs text-slate-500">
                Category
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedEquipment.category }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-4">
              <p class="text-xs text-slate-500">
                Location
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedEquipment.location }}
              </p>
            </div>

            <div class="rounded-xl bg-slate-50 p-4">
              <p class="text-xs text-slate-500">
                Assigned To
              </p>

              <p class="text-sm font-bold text-slate-900 mt-1">
                {{ selectedEquipment.assignedTo }}
              </p>
            </div>

          </div>


          <div class="border-t border-slate-200 pt-4 space-y-3">

            <div class="flex justify-between gap-4">
              <span class="text-sm text-slate-500">
                Last Inspection
              </span>

              <span class="text-sm font-semibold text-slate-900">
                {{ selectedEquipment.lastInspected }}
              </span>
            </div>

            <div
              v-if="selectedEquipment.nextInspection"
              class="flex justify-between gap-4"
            >
              <span class="text-sm text-slate-500">
                Next Inspection
              </span>

              <span class="text-sm font-semibold text-slate-900">
                {{ selectedEquipment.nextInspection }}
              </span>
            </div>

            <div
              v-if="selectedEquipment.notes"
              class="pt-2"
            >
              <p class="text-xs text-slate-500">
                Notes
              </p>

              <p class="text-sm text-slate-700 mt-1 leading-6">
                {{ selectedEquipment.notes }}
              </p>
            </div>

          </div>


          <div class="flex justify-end gap-3">

            <button
              @click="editEquipment(selectedEquipment)"
              class="px-5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-600 hover:bg-slate-50"
            >
              Edit
            </button>

            <button
              @click="selectedEquipment = null"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Close
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- REPORT ISSUE MODAL -->
    <!-- ========================================================= -->
    <div
      v-if="issueEquipment"
      class="fixed inset-0 z-50 bg-black/40 flex items-center justify-center p-4"
      @click.self="issueEquipment = null"
    >

      <div class="w-full max-w-lg bg-white rounded-2xl shadow-2xl overflow-hidden">

        <div class="px-6 py-5 border-b border-slate-200">

          <p class="text-xs font-bold text-[#8B1E23] uppercase tracking-wide">
            Equipment Issue
          </p>

          <h3 class="text-xl font-bold text-slate-900 mt-1">
            Report {{ issueEquipment.name }}
          </h3>

        </div>


        <div class="p-6">

          <label class="text-sm font-semibold text-slate-700">
            Issue Description
          </label>

          <textarea
            v-model="issueDescription"
            rows="5"
            placeholder="Describe the problem or damage..."
            class="w-full mt-2 px-4 py-3 rounded-xl border border-slate-300 text-sm outline-none resize-none focus:ring-2 focus:ring-[#8B1E23]/20"
          ></textarea>


          <div class="flex justify-end gap-3 mt-5">

            <button
              @click="issueEquipment = null"
              class="px-5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-600 hover:bg-slate-50"
            >
              Cancel
            </button>

            <button
              @click="submitIssueReport"
              class="px-5 py-2.5 rounded-xl bg-[#8B1E23] text-white text-sm font-bold hover:bg-[#72181D]"
            >
              Report Issue
            </button>

          </div>

        </div>

      </div>

    </div>


    <!-- ========================================================= -->
    <!-- TOAST -->
    <!-- ========================================================= -->
    <transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0 translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-200"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 translate-y-2"
    >

      <div
        v-if="toastMessage"
        class="fixed bottom-6 right-6 z-[70] bg-slate-900 text-white px-5 py-3 rounded-xl shadow-xl text-sm font-semibold"
      >
        {{ toastMessage }}
      </div>

    </transition>

  </div>
</template>


<script setup>
import { computed, onMounted, ref, watch } from 'vue'

const props = defineProps({
  currentUser: {
    type: Object,
    required: false,
    default: null
  },

  ICONS: {
    type: Object,
    required: true
  }
})


/* =========================================================
   STORAGE
   ========================================================= */

const STORAGE_KEY = 'fireNotifyPersonnelEquipment'


/* =========================================================
   EQUIPMENT DATA
   ========================================================= */

const equipment = ref([
  {
    id: 'FH-001',
    name: 'Fire Hose Reel',
    category: 'Firefighting Tools',
    location: 'Station 1',
    assignedTo: 'Engine 01',
    condition: 'Serviceable',
    lastInspected: 'September 5, 2026',
    nextInspection: 'October 5, 2026',
    notes: 'Ready for deployment.'
  },

  {
    id: 'SCBA-014',
    name: 'SCBA Set',
    category: 'Protective Equipment',
    location: 'Locker A-04',
    assignedTo: 'FO3 Juan Dela Cruz',
    condition: 'Serviceable',
    lastInspected: 'September 1, 2026',
    nextInspection: 'September 20, 2026',
    notes: 'Cylinder pressure: 3,000 PSI.'
  },

  {
    id: 'RAD-008',
    name: 'Portable Radio',
    category: 'Communication',
    location: 'Control Room',
    assignedTo: 'Station Communications',
    condition: 'For Maintenance',
    lastInspected: 'September 8, 2026',
    nextInspection: 'September 15, 2026',
    notes: 'Battery replacement required.'
  },

  {
    id: 'HYD-003',
    name: 'Hydraulic Cutter',
    category: 'Rescue Tools',
    location: 'Equipment Bay',
    assignedTo: 'FO1 Carlo Reyes',
    condition: 'Damaged',
    lastInspected: 'September 9, 2026',
    nextInspection: '',
    notes: 'Hydraulic leak detected.'
  },

  {
    id: 'MED-006',
    name: 'First Aid Kit',
    category: 'Medical Supplies',
    location: 'Response Vehicle 02',
    assignedTo: 'Response Team',
    condition: 'Audit Required',
    lastInspected: 'August 30, 2026',
    nextInspection: 'September 16, 2026',
    notes: 'Inventory count incomplete.'
  }
])


/* =========================================================
   FILTERS
   ========================================================= */

const categoryFilter = ref('All Categories')
const conditionFilter = ref('All Conditions')
const searchQuery = ref('')


const availableCategories = computed(() => {
  return [...new Set(equipment.value.map(item => item.category))]
})


const filteredEquipment = computed(() => {

  const query = searchQuery.value.trim().toLowerCase()

  return equipment.value.filter(item => {

    const matchesCategory =
      categoryFilter.value === 'All Categories' ||
      item.category === categoryFilter.value

    const matchesCondition =
      conditionFilter.value === 'All Conditions' ||
      item.condition === conditionFilter.value

    const searchText = [
      item.id,
      item.name,
      item.category,
      item.location,
      item.assignedTo,
      item.condition,
      item.notes
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    const matchesSearch =
      !query || searchText.includes(query)

    return (
      matchesCategory &&
      matchesCondition &&
      matchesSearch
    )
  })
})


const clearFilters = () => {
  categoryFilter.value = 'All Categories'
  conditionFilter.value = 'All Conditions'
  searchQuery.value = ''
}


/* =========================================================
   STATISTICS
   ========================================================= */

const totalEquipment = computed(() =>
  equipment.value.length
)


const serviceableCount = computed(() =>
  equipment.value.filter(
    item => item.condition === 'Serviceable'
  ).length
)


const maintenanceCount = computed(() =>
  equipment.value.filter(
    item => item.condition === 'For Maintenance'
  ).length
)


const criticalCount = computed(() =>
  equipment.value.filter(
    item =>
      item.condition === 'Damaged' ||
      item.condition === 'Missing'
  ).length
)


const serviceablePercentage = computed(() => {

  if (!totalEquipment.value) return 0

  return Math.round(
    (serviceableCount.value / totalEquipment.value) * 100
  )
})


/* =========================================================
   AUDIT
   ========================================================= */

const inspectedCount = computed(() => {

  return equipment.value.filter(
    item =>
      item.condition === 'Serviceable' ||
      item.condition === 'For Maintenance' ||
      item.condition === 'Damaged' ||
      item.condition === 'Missing'
  ).length
})


const auditProgress = computed(() => {

  if (!totalEquipment.value) return 0

  return Math.round(
    (inspectedCount.value / totalEquipment.value) * 100
  )
})


const remainingAudit = computed(() => {
  return Math.max(
    totalEquipment.value - inspectedCount.value,
    0
  )
})


/* =========================================================
   COMPLIANCE
   ========================================================= */

const complianceRate = computed(() => {

  if (!totalEquipment.value) return 0

  const readyItems = equipment.value.filter(
    item => item.condition === 'Serviceable'
  ).length

  return Math.round(
    (readyItems / totalEquipment.value) * 100
  )
})


/* =========================================================
   MAINTENANCE
   ========================================================= */

const maintenanceItems = computed(() => {

  return equipment.value
    .filter(
      item =>
        item.condition === 'For Maintenance' ||
        item.condition === 'Damaged' ||
        item.condition === 'Audit Required'
    )
    .map(item => ({
      id: item.id,
      name: item.name,
      dueDate:
        item.nextInspection || 'Immediate attention required',
      note:
        item.condition === 'Damaged'
          ? 'Repair required before deployment.'
          : item.condition === 'Audit Required'
            ? 'Inventory verification required.'
            : item.notes || 'Maintenance required.',
      urgent:
        item.condition === 'Damaged' ||
        item.condition === 'Missing'
    }))
})


/* =========================================================
   MODALS
   ========================================================= */

const showFormModal = ref(false)
const editingEquipment = ref(null)
const selectedEquipment = ref(null)
const issueEquipment = ref(null)
const issueDescription = ref('')


/* =========================================================
   FORM
   ========================================================= */

const defaultForm = () => ({
  id: '',
  name: '',
  category: 'Firefighting Tools',
  condition: 'Serviceable',
  location: 'BFP Balingasag',
  assignedTo: '',
  lastInspected: '',
  nextInspection: '',
  notes: ''
})


const form = ref(defaultForm())


const openAddModal = () => {

  editingEquipment.value = null
  form.value = defaultForm()

  showFormModal.value = true
}


const editEquipment = item => {

  selectedEquipment.value = null

  editingEquipment.value = item

  form.value = {
    ...item
  }

  showFormModal.value = true
}


const closeFormModal = () => {

  showFormModal.value = false
  editingEquipment.value = null
  form.value = defaultForm()
}


const saveEquipment = () => {

  if (editingEquipment.value) {

    const index = equipment.value.findIndex(
      item => item.id === editingEquipment.value.id
    )

    if (index !== -1) {
      equipment.value[index] = {
        ...form.value
      }
    }

    showToast('Equipment record updated successfully.')

  } else {

    const exists = equipment.value.some(
      item => item.id.toLowerCase() === form.value.id.toLowerCase()
    )

    if (exists) {
      showToast('Equipment ID already exists.')
      return
    }

    equipment.value.unshift({
      ...form.value
    })

    showToast('Equipment added successfully.')
  }

  closeFormModal()
}


/* =========================================================
   VIEW
   ========================================================= */

const viewEquipment = item => {
  selectedEquipment.value = item
}


/* =========================================================
   INSPECTION
   ========================================================= */

const markInspected = id => {

  const item = equipment.value.find(
    equipmentItem => equipmentItem.id === id
  )

  if (!item) return

  item.condition = 'Serviceable'
  item.lastInspected = formatDate(new Date())

  showToast(`${item.name} marked as inspected.`)
}


/* =========================================================
   REPORT ISSUE
   ========================================================= */

const reportIssue = item => {

  issueEquipment.value = item
  issueDescription.value = ''
}


const submitIssueReport = () => {

  if (!issueDescription.value.trim()) {
    showToast('Please describe the equipment issue.')
    return
  }

  issueEquipment.value.condition = 'Damaged'

  issueEquipment.value.notes =
    issueDescription.value.trim()

  issueEquipment.value.lastInspected =
    formatDate(new Date())

  issueEquipment.value = null
  issueDescription.value = ''

  showToast('Equipment issue reported successfully.')
}


/* =========================================================
   STYLES
   ========================================================= */

const getCardClass = condition => {

  const classes = {
    Serviceable: 'border-green-200 bg-green-50',
    'For Maintenance': 'border-yellow-200 bg-yellow-50',
    Damaged: 'border-red-200 bg-red-50',
    Missing: 'border-red-200 bg-red-50',
    'Audit Required': 'border-slate-200 bg-slate-50'
  }

  return classes[condition] || 'border-slate-200 bg-slate-50'
}


const getStatusClass = condition => {

  const classes = {
    Serviceable: 'bg-green-100 text-green-700',
    'For Maintenance': 'bg-yellow-100 text-yellow-700',
    Damaged: 'bg-red-100 text-[#8B1E23]',
    Missing: 'bg-red-100 text-[#8B1E23]',
    'Audit Required': 'bg-slate-200 text-slate-700'
  }

  return classes[condition] || 'bg-slate-100 text-slate-600'
}


const getIconBackground = condition => {

  const classes = {
    Serviceable: 'bg-green-100',
    'For Maintenance': 'bg-yellow-100',
    Damaged: 'bg-red-100',
    Missing: 'bg-red-100',
    'Audit Required': 'bg-slate-200'
  }

  return classes[condition] || 'bg-slate-100'
}


const getIconColor = condition => {

  const classes = {
    Serviceable: 'text-green-600',
    'For Maintenance': 'text-yellow-600',
    Damaged: 'text-[#8B1E23]',
    Missing: 'text-[#8B1E23]',
    'Audit Required': 'text-slate-600'
  }

  return classes[condition] || 'text-slate-600'
}


const getEquipmentIcon = condition => {

  if (condition === 'Serviceable') {
    return props.ICONS.check || ''
  }

  if (condition === 'For Maintenance') {
    return props.ICONS.clock || ''
  }

  if (condition === 'Damaged' || condition === 'Missing') {
    return props.ICONS.siren || ''
  }

  return props.ICONS.check || ''
}


/* =========================================================
   DATE
   ========================================================= */

const formatDate = date => {

  return new Intl.DateTimeFormat('en-PH', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date)
}


/* =========================================================
   LOCAL STORAGE
   ========================================================= */

onMounted(() => {

  const saved = localStorage.getItem(STORAGE_KEY)

  if (!saved) return

  try {

    const parsed = JSON.parse(saved)

    if (Array.isArray(parsed)) {
      equipment.value = parsed
    }

  } catch (error) {

    console.error(
      'Failed to load equipment records:',
      error
    )
  }
})


watch(
  equipment,
  value => {
    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify(value)
    )
  },
  { deep: true }
)


/* =========================================================
   TOAST
   ========================================================= */

const toastMessage = ref('')
let toastTimer = null


const showToast = message => {

  toastMessage.value = message

  clearTimeout(toastTimer)

  toastTimer = setTimeout(() => {
    toastMessage.value = ''
  }, 3000)
}
</script>